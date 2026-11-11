"""Offline checks for Bài 2: error handling and step limits."""
import json
import unittest

from agent import run_agent


def tool_call(call_id, name, arguments):
    call = {'id': call_id, 'name': name, 'arguments': arguments}
    message = {'role': 'assistant', 'content': None, 'tool_calls': [
        {'id': call_id, 'type': 'function', 'function': {'name': name, 'arguments': arguments}}
    ]}
    return {'message': message, 'calls': [call], 'finish': 'tool_calls', 'usage': {}}


def final(content='Đã trả lời', finish='stop'):
    return {'message': {'role': 'assistant', 'content': content},
            'calls': [], 'finish': finish, 'usage': {}}


class FakeProvider:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.histories = []

    def complete(self, messages, schemas):
        self.histories.append(list(messages))
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


class FakeTools:
    def __init__(self, result=None):
        self.result = result or {'ok': True, 'provider': 'github'}

    def execute(self, name, args):
        return self.result


class Bai2Tests(unittest.TestCase):
    def test_max_steps_counts_model_calls(self):
        provider = FakeProvider([tool_call('a', 'get_status', '{}'),
                                 tool_call('b', 'get_status', '{}')])
        result = run_agent('Kiểm tra', provider, FakeTools(), max_steps=2)
        self.assertEqual(result['status'], 'max_steps')
        self.assertEqual(len(provider.histories), 2)
        self.assertEqual(result['trace'][-1]['event'], 'max_steps')

    def test_invalid_json_is_observation(self):
        provider = FakeProvider([tool_call('a', 'get_status', '{'), final()])
        result = run_agent('Kiểm tra', provider, FakeTools())
        self.assertEqual(result['status'], 'completed')
        observation = json.loads(provider.histories[1][-1]['content'])
        self.assertEqual(observation['error'], 'INVALID_ARGUMENTS')
        self.assertEqual(provider.histories[1][-1]['tool_call_id'], 'a')

    def test_tool_failure_is_observation(self):
        provider = FakeProvider([tool_call('a', 'get_status', '{}'), final('Không đủ dữ liệu')])
        tools = FakeTools({'ok': False, 'error': 'TIMEOUT'})
        result = run_agent('Kiểm tra', provider, tools)
        self.assertEqual(result['status'], 'completed')
        self.assertEqual(json.loads(provider.histories[1][-1]['content'])['error'], 'TIMEOUT')
        self.assertFalse(next(x for x in result['trace'] if x['event'] == 'tool')['ok'])

    def test_provider_failure_ends_with_error(self):
        result = run_agent('Kiểm tra', FakeProvider([RuntimeError('HTTP 503')]), FakeTools())
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['trace'][-1]['event'], 'provider_error')

    def test_truncated_answer_is_error(self):
        result = run_agent('Kiểm tra', FakeProvider([final('Chưa xong', 'length')]), FakeTools())
        self.assertEqual(result['status'], 'error')
        self.assertEqual(result['trace'][-1]['event'], 'incomplete')


if __name__ == '__main__':
    unittest.main()

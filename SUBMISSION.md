# Hướng dẫn nộp bài · Day 04

**Hình thức: Bài cá nhân.** Mỗi cá nhân tự làm, tự tạo repo riêng và tự nộp link lên LMS bằng tài khoản cá nhân.

## Cấu trúc repo và file phải nộp

```text
K5-L3A-DAY04-[HoVaTen]-[MSSV]-ReactLoopAgent/
├── agent.py            <- agent loop đã hoàn thiện
├── eval_before.json    <- kết quả eval lần 1, đủ 22 case
├── eval_after.json     <- kết quả eval lần 2, đủ 22 case
├── NOTES.md            <- ghi chú phân tích
└── (giữ nguyên các file còn lại của repo đề)
```

Nếu làm thử thách bonus, nộp thêm `eval_bonus.json`. Các file eval phải đã xóa thông tin nhạy cảm. Không nộp file `.env` hay bất kỳ API key nào. Không sửa `fixtures/`, `evals/cases.json`, `evals/scenarios.py`, `evals/grading.py` để case pass.

Điểm tổng trong file eval phải khác `null`. Nếu là `null`, có case chưa chấm được: sửa cấu hình rồi chạy lại.

## Quy tắc đặt tên repo nộp

| Lớp | Tên repo |
|---|---|
| L3A | `K5-L3A-DAY04-[HoVaTen]-[MSSV]-ReactLoopAgent` |
| L3B | `K5-L3B-DAY04-[HoVaTen]-[MSSV]-ReactLoopAgent` |

`[HoVaTen]` và `[MSSV]` là phần thay đổi theo từng học viên. Thay bằng thông tin của bạn và bỏ cả dấu ngoặc vuông, ví dụ Nguyễn Văn A, MSSV 2A20260000, lớp L3A đặt là `K5-L3A-DAY04-NguyenVanA-2A20260000-ReactLoopAgent`. Viết không dấu, không khoảng trắng, nối các phần bằng dấu `-`.

## Cách tạo repo

1. Fork repo đề về tài khoản GitHub của bạn.
2. Vào Settings của repo vừa fork, đổi tên theo bảng trên.
3. Clone repo về máy, làm bài và push vào repo này.

Giữ repo ở chế độ public để bài chấm được.

## Nơi nộp

Dán link repo của bạn vào bài Day 04 trên LMS: **https://aithucchien.vinuni.edu.vn**. Mỗi cá nhân tự nộp link của mình bằng tài khoản cá nhân.

## Deadline (giờ Việt Nam, GMT+7)

| Ca học | Hạn nộp |
|---|---|
| 9:00–13:00 | 23:59 cùng ngày |
| 14:00–18:00 | 23:59 cùng ngày |
| 16:30–20:00 | 12:00 trưa hôm sau |

Hạn trên áp dụng trừ khi key coach thông báo khác trong vòng 48 giờ sau buổi lab. Nộp muộn bị trừ điểm, xem [RULES.md](RULES.md).

## Checklist trước khi nộp

- [x] `python3 -m unittest discover -s tests -v` không còn test lỗi. (42/42 OK)
- [x] `eval_before.json` và `eval_after.json` cùng agent model, judge model, snapshot, max steps và dataset. (`ckey` / `deepseek-v4.1-flash`, judge giống agent, `max_steps 8`, `core`; điểm 94.32 → 99.50, cả hai 22/22 đã chấm)
- [x] `NOTES.md` đã điền đủ 5 mục.
- [x] Repo không chứa `.env` hay API key. Kiểm tra bằng `git ls-files | grep .env`, chỉ được thấy `.env.example`.
- [x] Tên repo đúng quy tắc, đã thay `[HoVaTen]` và `[MSSV]`, mở được link khi chưa đăng nhập. (repo hiện tên `...-Day4-...`, quy tắc yêu cầu `...-DAY04-...`)
- [x] Đã dán link repo lên LMS trước hạn.
- [x] (Bonus) `python3 -m unittest discover -s bonus -p 'test_*.py' -v` không còn test lỗi. (3/3 OK)
- [x] (Bonus) `eval_bonus.json` đủ 10 case đã chấm, `bonus_points_0_15` khác `null`. (99.5/100 → 14.92/15)
- [x] (Bonus) `NOTES.md` có ghi chú retry, pagination, context và giới hạn.
- [ ] (Bonus) Commit và push `agent.py`, `eval_bonus.json`, `NOTES.md`.

# Koji — JLPT Study Agent

Ôn JLPT N5–N1 bằng sách của bạn, với ngôn ngữ bạn chọn. Giải đáp câu hỏi khó, chọn phần học vừa với thời gian hôm nay và tiếp tục từ chỗ đã dừng.

## Bắt đầu bằng một câu hỏi

**Trong cuộc trò chuyện AI bạn đang dùng:** tải lên hoặc dán [hướng dẫn Koji](../agent/COACH.md), rồi gửi câu hỏi. Khi cần, hãy kèm câu văn liên quan, các lựa chọn và đáp án của bạn. Dùng một đoạn trích ngắn hoặc ảnh rõ chữ mà công cụ trò chuyện có thể xử lý.

> Hãy làm theo hướng dẫn Koji này. Giải thích bằng tiếng Việt. Tôi chọn B nhưng đáp án ghi C. Đây là đoạn văn và cách tôi suy luận. Vì sao C phù hợp hơn?

**Trong Codex hoặc Claude Code có quyền truy cập tệp:** [tải kho mã này](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), giải nén và mở thư mục. Hãy yêu cầu:

> Đọc AGENTS.md và giúp tôi học với Koji. Giải thích và ghi chép cá nhân bằng tiếng Việt. Đây là câu hỏi của tôi trong sách.

Bạn có thể viết cả hai yêu cầu bằng ngôn ngữ của mình. Không cần máy chủ Koji, ứng dụng riêng, cài Python hay khóa API cho dự án. Bạn cần sử dụng được một trợ lý AI có thể đọc hướng dẫn; hạn mức và chi phí của dịch vụ đó vẫn áp dụng.

## Hoặc chọn nội dung học hôm nay

Cho Koji biết bạn đang mở phần nào của sách và có bao nhiêu thời gian. Bổ sung cấp độ JLPT mục tiêu nếu chưa được biết.

> Tôi đang ôn N3. Tôi ở đầu phần ngữ pháp này và có 25 phút. Giúp tôi chọn nội dung học hôm nay.

Koji đề xuất điểm bắt đầu, điểm dừng và phân bổ thời gian gồm ôn tập, hỏi đáp và tổng kết ngắn. Chỉ tên sách không đủ để suy ra trang hoặc nội dung. Bạn có thể bắt đầu từ một phần trước khi lập kế hoạch cho cả kỳ thi.

## Kết thúc bằng một tin nhắn

> Tôi đã làm xong câu 1–4 trong 18 phút. Câu 3 cần gợi ý. Tiếp theo là câu 5.

Koji tóm tắt những gì bạn thực sự đã làm, điều còn chưa rõ và chỗ để học tiếp. Đặt câu hỏi không tự động được tính là trả lời sai; đáp án có gợi ý được phân biệt với đáp án tự làm.

Khi quyền truy cập tệp hoạt động, Koji lưu và kiểm tra bản ghi hiện tại tại `local/CURRENT.md`, kèm ghi chép các buổi học. Trong trò chuyện thông thường, Koji đưa ra một ghi chú học tập ngắn gọn đã cập nhật để bạn tự lưu. Tạo ghi chú không có nghĩa là tự động lưu vào máy.

## Quay lại và tiếp tục

> Tiếp tục nhé. Hôm nay tôi có 15 phút.

Giữ nguyên thư mục học hoặc cung cấp ghi chú đã lưu mới nhất trong cuộc trò chuyện mới. Koji dùng bằng chứng liên quan từ trước để đề xuất ôn ngắn và nhiệm vụ tiếp theo trong sách. Ví dụ, trước khi học tiếp, bạn có thể được kiểm tra nhanh xem đã tự phân biệt được điều từng cần gợi ý hay chưa.

Sau một thời gian nghỉ, hãy nói rõ:

> Tôi đã nghỉ học một tuần. Hôm nay có 10 phút.

Koji bắt đầu từ tiến độ đã xác nhận và giảm nhiệm vụ cho vừa thời gian. Những ngày bỏ lỡ không trở thành số giờ học bù bắt buộc. Bạn cũng có thể yêu cầu nhìn lại tuần học, sửa bản ghi, xuất ghi chú hiện tại hoặc nói “đừng lưu buổi học này”.

## Ghi chú phát triển cùng việc học

Hướng dẫn là men khởi đầu; việc học cung cấp nguyên liệu. Những giải thích hữu ích lặp lại có thể trở thành các trang kiến thức liên kết, tách biệt với bằng chứng về điều bạn có thể trả lời. Bạn không cần tự sắp xếp thư mục hay duy trì thêm một cuốn sổ.

Tệp học tập nằm trong `local/`, mặc định được loại khỏi Git. Giữ thư mục này khi cập nhật Koji; thay các tệp hướng dẫn dùng chung, không thay bản ghi học tập. Lưu cục bộ không có nghĩa là AI xử lý ngoại tuyến. Koji hoạt động trong các cuộc trò chuyện, không nhắc nhở chạy nền hay tự đồng bộ giữa các bản sao.

Giải thích và ghi chú theo lựa chọn ngôn ngữ của bạn, kèm ví dụ tiếng Nhật và cách đọc kanji. Hướng dẫn được viết bằng tiếng Anh. Các bản dịch README do AI viết và chưa được người bản ngữ đánh giá độc lập; bản tiếng Anh là bản tham chiếu.

## Ngôn ngữ README

- [English](../README.md)
- [한국어](README.ko.md)
- [日本語](README.ja.md)
- [Español](README.es.md)
- [Français](README.fr.md)
- [Deutsch](README.de.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)
- [Português (Brasil)](README.pt-BR.md)
- [Italiano](README.it.md)
- [Русский](README.ru.md)
- [Українська](README.uk.md)
- [Polski](README.pl.md)
- [Nederlands](README.nl.md)
- [Svenska](README.sv.md)
- [Dansk](README.da.md)
- [Norsk (bokmål)](README.no.md)
- [Suomi](README.fi.md)
- [Čeština](README.cs.md)
- [Türkçe](README.tr.md)
- [Bahasa Indonesia](README.id.md)
- [Tiếng Việt](README.vi.md)
- [ไทย](README.th.md)
- [हिन्दी](README.hi.md)
- [বাংলা](README.bn.md)
- [العربية](README.ar.md)
- [فارسی](README.fa.md)
- [עברית](README.he.md)
- [Bahasa Melayu](README.ms.md)
- [Filipino](README.tl.md)

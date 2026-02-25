# [cite_start]Xây dựng mô hình dự đoán tính cách người dùng mạng xã hội từ bộ dữ liệu MBTI [cite: 1, 2]

**Môn học:** IE403 - Phân tích và thiết kế hệ thống thông tin
**Giảng viên hướng dẫn:** ThS. Huỳnh Văn Tín, ThS. [cite_start]Nguyễn Văn Kiệt [cite: 4]
[cite_start]**Nhóm thực hiện:** Nhóm 10 [cite: 3, 8]
* Lê Vũ Khánh Thảo - 23521469
* Hoàng Ngọc Quý - 21522529
* Trần Hoàng Nguyên - 21522396
* Nguyễn Đức Thịnh - 21522636
* Hoàng Anh Dũng - 20521206

---

## 1. Giới thiệu dự án
[cite_start]Dự án tập trung nghiên cứu việc áp dụng các kỹ thuật Xử lý ngôn ngữ tự nhiên (NLP) và Học máy để dự đoán 4 cặp tính cách đối ngẫu theo mô hình MBTI (I-E, N-S, T-F, J-P) từ dữ liệu văn bản mạng xã hội[cite: 11, 25]. [cite_start]Nghiên cứu giải quyết bài toán phân loại văn bản đa nhãn trong bối cảnh dữ liệu thực tế bị nhiễu và mất cân bằng lớp nghiêm trọng[cite: 22, 23, 26].

## 2. Mục tiêu nghiên cứu
* [cite_start]**Xây dựng và tối ưu hóa mô hình:** Thử nghiệm từ các mô hình truyền thống (Logistic Regression, SVM) đến học sâu (LSTM, CNN) và mô hình ngôn ngữ lớn (RoBERTa)[cite: 24].
* [cite_start]**Giải quyết thách thức dữ liệu:** Xử lý vấn đề mất cân bằng lớp (Class Imbalance) và ngăn chặn rò rỉ dữ liệu (Anti-Data Leakage)[cite: 26].
* [cite_start]**Đánh giá thực nghiệm:** So sánh hiệu suất giữa các mô hình đơn giản và phức tạp để tìm ra sự đánh đổi tối ưu giữa chi phí và độ chính xác[cite: 27, 28].

## 3. Dữ liệu (Dataset)
[cite_start]Đồ án sử dụng song song hai bộ dữ liệu từ Kaggle để đối chứng hiệu năng[cite: 84]:
* [cite_start]**mbti_1:** 8.675 mẫu thu thập từ diễn đàn PersonalityCafe[cite: 85, 309].
* [cite_start]**MBTI 500:** 106.000 bản ghi từ Reddit và PersonalityCafe, mỗi mẫu được chuẩn hóa ở độ dài 500 từ[cite: 88, 90, 311].


* **Link Dataset:** [https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset, https://www.kaggle.com/datasets/datasnaek/mbti-type]

## 4. Phương pháp và Mô hình
[cite_start]Nhóm đã triển khai quy trình thực nghiệm toàn diện gồm[cite: 115, 129]:
1. [cite_start]**Tiền xử lý:** Làm sạch nhiễu, xóa URL/Emoji và đặc biệt là xóa 16 từ khóa định danh tính cách.[cite: 116, 117, 122].
2. [cite_start]**Biểu diễn văn bản:** Sử dụng TF-IDF, Word Embeddings (GloVe, FastText) và Contextual Embeddings (RoBERTa)[cite: 61, 64, 67].
3. [cite_start]**Kiến trúc mô hình:** * **Baseline:** Logistic Regression và SVM[cite: 69].
   * [cite_start]**Deep Learning:** TextCNN và LSTM[cite: 73].
   * [cite_start]**SOTA:** RoBERTa (Fine-tuning với chiến thuật Head + Tail)[cite: 136, 141].

## 5. Kết quả đạt được
* [cite_start]**Hiệu ứng dữ liệu lớn:** Việc mở rộng lên bộ MBTI-500 giúp hiệu suất tăng từ 10% - 20% trên tất cả các mô hình[cite: 243].
* [cite_start]**Xếp hạng hiệu năng:** Nhóm mô hình Baseline (Logistic/SVM) giữ vững vị trí số 1 về tính ổn định và hiệu quả trên dữ liệu văn bản mạng xã hội[cite: 231].
* [cite_start]**Bứt phá trục NS:** Đạt độ chính xác cao nhất (>91% với LinearSVC)[cite: 235].
* [cite_start]**Cải thiện trục JP:** Tăng trưởng mạnh nhất khi có dữ liệu lớn, đưa hiệu suất từ mức "đoán mò" (55%) lên mức khả dụng (~75%)[cite: 226, 237].

---
[cite_start]© 2026 - Nhóm 10 - Faculty of Information Science and Engineering, UIT[cite: 5].

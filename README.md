# Xây dựng mô hình dự đoán tính cách người dùng mạng xã hội từ bộ dữ liệu MBTI.
**Môn học:** IE403 - Phân tích và thiết kế hệ thống thông tin
**Giảng viên hướng dẫn:** ThS. Huỳnh Văn Tín, ThS. Nguyễn Văn Kiệt 
**Nhóm thực hiện:** Nhóm 10
* Lê Vũ Khánh Thảo - 23521469
* Hoàng Ngọc Quý - 21522529
* Trần Hoàng Nguyên - 21522396
* Nguyễn Đức Thịnh - 21522636
* Hoàng Anh Dũng - 20521206

---

## 1. Giới thiệu dự án
Dự án tập trung nghiên cứu việc áp dụng các kỹ thuật Xử lý ngôn ngữ tự nhiên (NLP) và Học máy để dự đoán 4 cặp tính cách đối ngẫu theo mô hình MBTI (I-E, N-S, T-F, J-P) từ dữ liệu văn bản mạng xã hội[cite: 11, 25]. [cite_start]Nghiên cứu giải quyết bài toán phân loại văn bản đa nhãn trong bối cảnh dữ liệu thực tế bị nhiễu và mất cân bằng lớp nghiêm trọng.
## 2. Mục tiêu nghiên cứu
* **Xây dựng và tối ưu hóa mô hình:** Thử nghiệm từ các mô hình truyền thống (Logistic Regression, SVM) đến học sâu (LSTM, CNN) và mô hình ngôn ngữ lớn (RoBERTa).
* **Giải quyết thách thức dữ liệu:** Xử lý vấn đề mất cân bằng lớp (Class Imbalance) và ngăn chặn rò rỉ dữ liệu (Anti-Data Leakage).
* **Đánh giá thực nghiệm:** So sánh hiệu suất giữa các mô hình đơn giản và phức tạp để tìm ra sự đánh đổi tối ưu giữa chi phí và độ chính xác.

## 3. Dữ liệu (Dataset)
Đồ án sử dụng song song hai bộ dữ liệu từ Kaggle để đối chứng hiệu năng:
* **mbti_1:** 8.675 mẫu thu thập từ diễn đàn PersonalityCafe.
* **MBTI 500:** 106.000 bản ghi từ Reddit và PersonalityCafe, mỗi mẫu được chuẩn hóa ở độ dài 500 từ.


* **Link Dataset:** [https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset, https://www.kaggle.com/datasets/datasnaek/mbti-type]

## 4. Phương pháp và Mô hình
Nhóm đã triển khai quy trình thực nghiệm toàn diện gồm:
1. **Tiền xử lý:** Làm sạch nhiễu, xóa URL/Emoji và đặc biệt là xóa 16 từ khóa định danh tính cách.
2. **Biểu diễn văn bản:** Sử dụng TF-IDF, Word Embeddings (GloVe, FastText) và Contextual Embeddings (RoBERTa).
3. **Kiến trúc mô hình:**
   * **Baseline:** Logistic Regression và SVM.
   * **Deep Learning:** TextCNN và LSTM.
   * **SOTA:** RoBERTa.

## 5. Kết quả đạt được
* **Hiệu ứng dữ liệu lớn:** Việc mở rộng lên bộ MBTI-500 giúp hiệu suất tăng từ 10% - 20% trên tất cả các mô hình.
* **Xếp hạng hiệu năng:** Nhóm mô hình Baseline (Logistic/SVM) tốt nhất về tính ổn định và hiệu quả trên dữ liệu văn bản mạng xã hội.
* **Bứt phá trục NS:** Đạt độ chính xác cao nhất (>91% với LinearSVC).
* **Cải thiện trục JP:** Tăng trưởng mạnh nhất khi có dữ liệu lớn, đưa hiệu suất từ mức "đoán mò" (55%) lên mức khả dụng (~75%).

---
© 2026 - Nhóm 10 - Faculty of Information Science and Engineering, UIT.

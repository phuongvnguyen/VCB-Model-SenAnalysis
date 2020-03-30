#!/usr/bin/env python
# coding: utf-8

# 
# 
# $$\Large \underline{\color{red}{\textbf{BÁO CÁO}}}$$
# 
# 
# 
# $$\Large \color{blue}{\textbf{Giới Thiệu Cách Thức Tính Toán Và Áp Dụng Hơn 35 Chỉ Tiêu Và Phương Pháp}}$$
# $$\Large \color{blue}{\textbf{Theo Chuẩn Mực Quốc Tê Được Sử Dụng Cho Qúa Trình}}$$
# $$\Large \color{blue}{\textbf{Phân Tích Độ Nhạy Trong Việc Đánh Gía Và Giám Sát Hoạt Động}}$$
# $$\Large \color{blue}{\textbf{Của Mô Hình Dự Báo Rủi Ro Vỡ Nợ}}$$
# $$\Large \color{blue}{\textbf{Trong Hoạt Động Tín Dụng Của Ngân Hàng}}$$
# 
# 
# $$\small \color{green}{\textbf{Đức, Ngày 20 Tháng 03 Năm 2020}}$$
# 
# 
# $$\small \color{green}{\textbf{Người thực hiện}}$$
# $$\large \color{green}{\textbf{NCS. Phuong Van Nguyen}}$$
# $$\small \color{red}{\textbf{ phuong.nguyen@summer.barcelonagse.eu}}$$
# $$\small \color{red}{\textbf{ phuong.nguyen@economics.uni-kiel.de}}$$
# $$\small \color{red}{\textbf{ phuongnv@iuj.ac.jp}}$$
# 
# 
# 
# $\underline{\color{blue}{\textbf{I. Giới Thiệu}}}$
# 
# $\underline{\color{blue}{\textbf{1. Động Cơ Và Mục Tiêu Của Dự Án}}}$
# 
# Vào tháng 6/2004, Uỷ Ban Basel về Giám Sát Hoạt Động Ngân Hàng đã phát hành phiên bản sửa đổi cho Basel II về Quy Chuẩn Quốc Tế Chung Cho Đo Lường và Tiêu Chuẩn Vốn (International Convergence of Capital Measurement and Capital Standards). Theo đó, các Ngân hàng và Tổ Chức Tín Dụng được phép sử dụng các Mô Hình nội bộ của họ cho kiểm soát tín dụng để đảm bảo những yêu cầu tối thiểu về vốn. Trước những yêu cầu đó, rõ ràng là việc phát triển các phương pháp để phân tích độ nhạy cho việc kiểm định và giám sát các Mô hình Xếp Hạng Tín Dụng Nội Bộ (IRB) trở lên vô cùng quan trọng, trong việc đảm bảo hoạt động ngân hàng theo tiêu chuẩn của Basel II.
# 
# Hoạt động hiệu của Mô Hình Xếp Hạng Tín Dụng Nội Bộ (IRB), là tiền để để ngân hàng tính toán được các chỉ tiêu quan trọng cho kiểm soát rủi ro tín dụng, như
# 
# - Probability of Default (PD):  Xác xuất Vỡ Nợ.
# - Loss Given Default (LGD): Khoản Lỗ Sau Khi Xử Lý Nợ, như bằng cách bán Nợ, Trong Tình Huống Vỡ Nợ Xảy Ra (.
# - Exposure At Default (EAD): Tổng Khoản Lỗ Trong Tình Huống Vỡ Nợ Xảy Ra.
# - Expected Loss: Khoản Lỗ Kỳ Vọng Nếu Xả Ra Vỡ Nợ (Expected Loss=PD*LGD*EAD)
# 
# Chính vì vậy, trong dự án này, mục tiêu chính của chúng tôi đó là trên cơ sở $\textbf{Khuyến Nghị của Uỷ Ban Basel II về giám sát Hoạt động Ngân hàng}$ và thực hành tại hệ thống Ngân hàng trên thé giới như ECB, Deutsche Bundesbank, Moody, Deloite, etc, các Tài Liệu Thống Kê, Toán Kinh Tế Lượng, chúng tôi
# 
# 
# $$\color{green}{\textbf{Giới thiệu trên 35 công cụ và chỉ tiêu thống kê}}$$
# 
# 
# được sử dụng cho $\textbf{phân tích Độ Nhạy trong quá trình kiểm định và giám sát hoạt động}$ của Mô hình Xếp Hạng Tín Dụng Nội Bộ, cụ thể ở đây là Mô Hình Logistic.
# 
# Mặc dù theo khuyến nghị của Uỷ Ban Basel (Basel Accords II) thì chỉ cần hai chỉ tiêu
# 
# 1. Accuracy Ratio
# 
# 2. Receiver Operating Characteristic
# 
# là đủ để phân tích Độ Nhạy cho Kiểm định và giám sát Mô Hình nội bộ. Tuy nhiên, vì khuyến nghị của Ủy Ban Basel không phải là yêu cầu bắt buộc với tất cả các Hệ Thống Ngân hàng trên toàn thế giới, mà nó chỉ mang tính tham khảo. Do đó, trong Dự Án này chúng tôi không đưa ra kết luận cụ thể công cụ thể hay chỉ tiêu nào tốt nhất để Phân tích độ nhạy cho việc kiểm định và giám sát Mô Hình Logistic. Thực tế là khi chúng tôi tham khảo các chỉ tiêu, phương pháp Phân tích độ nhạy cho việc Kiểm định và giám sát Mô Hình nội bộ của các Ngân Hàng Trung Ương(NHTW) trên Thế Giới, như ECB, NHTW Đức (Deutsche Bundesbank), NHTW Ba Lan, NHTW Bồ Đảo Nha, một loạt các định chế tài chính, như Moody, Deloite, etc. thì đều có những cách tiếp cận khác dựa trên cơ sở khuyến Nghị của Basel II. 
# 
# Thêm nữa, cũng chính Uỷ Ban Basel II, trong tài liệu $\textbf{"Studies on the Validation of Internal Rating System, Working Paper No.14, Revisied Version, May 2005"}$, tại trang 29, họ ghi như sau:
# 
# $$\small \color{red}{\text{"The choice of a specific technique to be applied for validation should
# depend upon the nature of the portfolio }}$$
# $$\small \color{red}{\text{under consideration. Retail portfolios or portfolios of
# small- and medium-sized enterprises with large records }}$$
# $$\small \color{red}{\text{of default data are much easier to
# explore with statistical methods than, for example,portfolios of sovereigns}}$$ $$\small \color{red}{\text{or financial 
# institutions where default data are sparse."}}$$
# 
# 
# 
# 
# ![Finity.png](attachment:Finity.png)
# 
# $$\text{Nguồn: https://www.finity.com.au/}$$
# 
# 
# $\underline{\color{blue}{\textbf{2. Hạn Chế của Dự Án}}}$
# 
# Mặc dù Phân tích độ nhạy cho việc kiểm định  và giám sát mô hình là quan trọng. Tuy nhiên, đây không phải là bước duy nhất trong việc đảm bảo mô hình hoạt động hiệu quả. Các vần đề quan trọng khác liên quan tới phát triên mô hình, chúng tôi sẽ không đề cập trong dự án này, sẽ liệt kê ra ở dưới đây
# 
# 
# - Thứ nhất, liên quan tới dữ liệu, cũng là một vấn đề $\textbf{then chốt}$ đảm bảo chất lượng của mô hình. Cụ thể hơn, nếu dữ liệu đầu vào bị $\textbf{mất cân đối}$ và không được xử lý bằng các kỹ thuật như: Over-sampling, Under-sampling, và Synthetic Minority Oversampling Technique (SMOTE), trước khi đào tạo mô hình, thì $\textbf{chắc chắn rằng}$ mô hình tạo ra sẽ hoạt động không hiểu quả. Và vấn đề $\textbf{mất cân đối}$ dữ liệu lại là vấn đề $\textbf{Phổ biến}$ trong bài toán thực tế. Ví dụ như, số lượng khách hàng Vỡ nợ sẽ $\textbf{luôn luôn}$ là ít hơn số lượng khác hàng không vỡ nợ
# 
# - Thứ hai, trong dữ liệu thô thực tế, có tới hàng trăm các biến số liên quan tới hoạt động tín dụng trong ngân hàng. Vậy chúng ta có nên đưa hết tất cả các biến đó vào trong mô hình? Hay làm thế nào để chọn biến vào mô hình? Để làm việc này, một trong những Thuật Toán chúng ta có thể áp dụng đó là Principal Component Analysis (PCA). Do đó, nếu bước này chúng ta không làm tốt thì $\textbf{chắc chắn rằng}$ mô hình tạo ra sẽ hoạt động không hiểu quả, etc.
# 
# - Thứ ba, Mô hình Logistic $\textbf{chắc chắn là}$ chưa phải một mô hình tối ưu nhất trong giải quyết bài toán dự báo rủi ro vỡ nợ trong hoạt động ngân hàng. Còn rất nhiều Mô hình và đặc biệt các chương trình Máy Học hoặc Deep Learning sử dụng các thuật toán hiện đại, có khả năng dự báo $\textbf{tốt hơn}$ rất nhiều Mô hình Logistic, chẳng hạn như Extreme Gradient Boosting, Long Short-Term Memory (LSTM), etc
# 
# - etc..
# 
# Nhờ có được các chương trình học bổng toàn phần từ IMF, Graduate School Scholarship Program (GSSP), quý DAAD Research Allowance, mà chúng tôi đã có được sự đào tạo bài bản về chuyên môn ở các cấp độ Ths và TS ở các quốc gia tiên tiến: Nhật Bản, Đức và các chương trình ngắn hạng ở Châu Âu, kết hợp với kinh nghiệm thời làm việc tại Phòng Mô Hình Hóa, Ngân Hàng Trung Ương Thụy Điển (Sveriges Riksbank), nếu được Qúy Ngân hàng trao cơ hội, chúng tôi hoàn toàn tự tin giải quyết được tất cả các vấn đề đã nêu ra ở trên và các yêu cầu khác của VCB.
# 
# 
# $\underline{\color{blue}{\textbf{3. Dữ Liệu}}}$
# 
# Để thực, hiện Dự An này, chúng tôi sử dụng dữ liệu về Vỡ Nợ của thẻ tín dụng, tại Kho Dữ Liệu của Trung Tâm Nghiên cứu Máy Học và Trí Tuệ Thông Minh Nhân Tạo thuộc Đại Học California, Irvine. Chi tiết về dữ liệu và tải dữ liệu có thể tải tại đường dẫn dưới đây.
# 
# https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients
# 
# $\underline{\color{blue}{\textbf{4. Phương Thức Thực Hiện}}}$
# 
# - Thứ nhất, Theo như khuyến nghị của Uỷ Ban Basel, cũng như các kỹ thuật trong Máy Học, chúng tôi tiến hành Phân tích Độ Nhạy cho kiểm định và giám sát Mô hình ở cả mảng In-Sample và cả Out-Of-Sample. Trong đó, phần  $\color{blue}{\textbf{Out-of-sample}}$ sẽ được coi như phần giám sát mô hình $\color{blue}{\textbf{(Model Monitoring)}}$
# . Để làm điều đó, chúng tôi chia dữ liệu theo tỷ lệ phân chia 70/30. Chú ý rằng, thông thường việc chia này phải được thực hiện một cách ngẫu nhiên $\textbf{random split}$, tuy nhiên trong tình huống này, để đơn giản, chúng tôi sẽ lấy 21000 quan sát đầu tiên trong bộ dữ liệu để đào tạo mô hình, và số còn lại là để giám sát mô hình.
# 
# ![SplitingDat.png](attachment:SplitingDat.png)
# 
# 
# - Thứ hai, quá trinh thực nghiệm Dự Án, chúng tôi sử dụng Ngôn Ngữ Lập Trình Python. Ngoài ra, chúng tôi hoàn toàn có thể phân tích thực nghiệm dự án này bằng các ngôn ngữ máy tính khác như R hay Matlab theo yêu cầu của Qúy Phòng.
# 
# $\underline{\color{blue}{\textbf{5. Kết quả dự án và Khuyến Nghị}}}$
# 
# 
# Trong thời gian 1 tuần nghiên cứu và thực hiện, chúng tôi đã hoàn thành giới thiệu cách tính toán của hơn $\underline{\color{blue}{\textbf{35 chỉ tiêu}}}$ phục vụ cho quá trình phân tích độ nhạy trong kiểm định và giám sát hoạt động của Mô Hình Logistic nói riêng, và các Mô hình Xếp Hạng Tín Dụng Nội Bộ (IRB) nói chung. Kết quả đạt được đó là, Dự án này đã giới thiệu và trình bày cách tính toán tất cả các chỉ tiêu, phương thức không chỉ theo khuyến nghị của Uỷ Ban Basel (Basel II) mà còn của các Hệ Thống Ngân hàng, các tổ chức tài chính trên thế giới. 
# 
# 
# 
# 
# 
# Phát triển mô hình đánh giá rủi ro đóng vai trò tối quan trọng trong hoạt động ngân hàng. Các mô hình kinh tế lượng với phương pháp tiếp cận truyền thống (frequentist) như OLS, Maximum Likelihood, hiện tại đã thể hiện những bất cập trong ước lượng hệ số mô hình, cụ thể giá trị P-value không còn tin tưởng sử dụng để đánh giá mô hình. Thay thế khuyến điểm đó, Bayesian econometrics được sử dụng rổng rãi hơn. Tuy nhiên, góc độ Industry thì Chương Trình Máy Học/AI đang được sử dụng rộng rãi trong mọi mặt của đời sống, trong đó Logistic chỉ là một Thuật toán trong nhiều Thuật toán được sử dụng để "Dạy khôn" chúng. Do đó, qua đề tài này chúng tôi muốn đưa ra khuyến nghị là phát triển các chương trình Máy Học/AI để dự báo rủi ro trong hoạt động ngân hàng. Dựa vào bộ dự liệu trong dự án này, chúng tôi có thể phát triển chương trình máy học, có khả năng dự báo chính xác rủi ro Vỡ Nợ của Ngân hàng với $\textbf{độ chính xác rất vượt}$ trội so với Mô hình Logistic. Tuy nhiên, do yêu cầu của dự án nên chúng tôi không giới thiệu việc phát triển Máy Học/AI mà tập trung đi xâu vào góc độ Phân Tích Độ Nhạy của mô hình Logistic. Hy vọng, sẽ có cơ hội phát triển xây dựng một chương trình Máy Học/AI trong dự báo rủi ro tín dụng trong hoạt động Ngân hàng tại Qúy Phòng.
# 
# 4. $\textbf{Độ Nhạy của Mô Hình Logistic với Độ Nhạy của các Mô hình khác}$: Khi đặt giả định là cố định số biến đầu vào, thì Độ Nhạy của Mô Hình Logistic trong trường hợp này, kém so với các Mô Hình khác như KNeighborsClassifier, SGDClass, RidgeClass, và NearCent. Trong trường hợp này, chúng ta đo lường Độ Nhạy/Khả năng phản ứng của Mô Hình bằng chỉ số Accurracy.
# 
# $\underline{\color{blue}{\textbf{5. Tài Liệu Tham Khảo}}}$
# 
# Trong quá trình thực hiện Dự An Phân Tích Độ Nhạy của Mô Hình Logistic, chúng tôi đã tham khảo rất nhiều nguồn từ Industry cũng như trong Academic. Từ đó, chúng tôi nhận thấy rằng khái niệm này là rất rộng. Tuy nhiên, để tránh tình trạng lang man, không có một hướng đi cụ thể rõ ràng cho Phân Tích Độ Nhạy (Sensitivity Analysis), thì chúng tôi tiến hành tập hợp và tổng hợp để chọn ra một cách tiệm cận cho hướng đi của Dự án này. Cụ thể, tiêu chí lựa chọn của chúng tôi đó là lọc ra những khái niệm có tính chất chung và tổng quát nhất về Phân Tích Độ Nhạy (Sensitivity Analysis) sử dụng cho giám sát và kiểm định Mô Hình. 
# 
# 
# Ví dụ, liên quan tới Banking Industry,  Chúng Tôi đặc biệt chú ý tới những Khuyến Nghị của Uỷ Ban Basel Về Giám Sát Hoạt Động Ngân hàng (Basel II). Cụ thể, đó là Tài Liệu, $\textbf{"Studies on the Validation of Internal Rating Systems" Revised Version, May 2005}$. Lý do chính chúng tôi sử dụng Khuyến Nghị của Uỷ Ban Basel, bởi đây là những khuyến nghị chuẩn dành cho tất cả các Ngân hàng trên toàn thế giới, trong việc phân tích đánh giá và giám sát các mô hình phân loại rủi ro nội bộ trong mỗi ngân hàng. Mặc dù, hiện tại sau Khủng Hoảng tài chính 2008, hiện nay Basel III đã được triển khai. Tuy nhiên, do hệ thống Ngân hàng Việt Nam vẫn đang triển khai hoạt động giám sát ngân hàng theo khuyến Nghị của Basel II, cho nên trong dự án này chúng tôi đặc biệt xây dựng và giới thiệu quy trình các chỉ tiểu sử dụng cho phân tích độ nhạy trong kiểm định và giám sát Mô hình Logistic của VCB. Thêm vào đó, việc áp dụng của Uỷ Ban Basel chỉ mang tính tham khảo, không có tính bắt buộc với hệ thống Ngân hàng trên toàn thế giới. Do đó, ngoài việc sử dụng những Khuyến Nghị của Uỷ Ban Basel, trong dự án này chúng tôi cũng tham khảo hoạt động Phân tích Độ nhạy cho việc Đánh giá và giám sát mô hình nội bổ của các quốc gia trên thế giới, như Ngân hàng Trung ương (NHTW) Châu Âu (ECB), NHTW Đức (Deutsche Bundesbank), etc và các công ty tài chính trên thế giới như Moody, Deloite, etc
# 
# 1. Basel Committee on Banking Supervision. Studies on the Validation of Internal Rating Systems. Working Paper No. 14, Revised version, May 2005.
# 
# 2. Natalia Nehrebecka. Approach to the assessment of credit risk for non-financial corporations. Poland Evidence
# 
# 3. Bernd Engelmann, Evelyn Hayden, Dirk Tasche. Measuring the Discriminative Power of Rating Systems. Discussion paper Series 2: Banking and Financial Supervision No 01/2003.
# 
# 4. Bernd Engelmann, Robert Rauhmeier. The Basel II Risk Parameters: Estimation, Validation Testing with Application to Loan Risk Management. Second Edition, Springer.
# 
# 5. Stefan Blochwitz, Thilo Liebig, Mikael Nyberg. Benchmarking Deutsche Bundesbank’s Default Risk Model, the
# KMV@ Private Firm Model@ and Common Financial Ratios for German Corporations. 2000
# 
# 6. Audrey Mauguen and Colin B. Begg. Using the Lorenz Curve to Characterize Risk Predictiveness and Etiologic Heterogeneity
# 
# 7. Mark Goldburd, Anand Khare, Dan Tevet, Dmitriy Guller. GENERALIZED LINEAR MODELS FOR INSURANCE RATING. Second Edition
# 
# 8. Michael J. Budinger; Ryan A. Michalik. Credit risk rating model validation: getting full value from an important process.
# 
# 9. Moody's Analytics. Model Monitoring: Independence, Speed and Accuracy.
# 
# 10. John Yick, Michael McLaon. To Freak Out or to Chill Out? A Guide to Model Monitoring. Finity Personal Lines Pricing And Portfolio Management Seminar, 2014.
# 
# 11. Accenture. Credit Risk Model Monitoring.
# 
# 12. Saltelli, A.; Ratto, M.; Andres, T.; Campolongo, F.; Cariboni, J.; Gatelli, D.; Saisana, M.; Tarantola, S. (2008). Global Sensitivity Analysis: The Primer. John Wiley & Sons.
# 
# 
# 13. Saltelli, A.; Ratto, M.; Campolongo, F.; Cariboni, J.; Gatelli, D.; Saisana, M.; Tarantola, S. (2008). Sensitivity Analysis In Practice: A Guide to Scientist Models.
#  
#  
# 14. Jeffrey M.Wooddridge. Introductory Econometrics: A Modern Approach, 2013.
#  
# 15. Ruey S.Tsay. Analysis of Financial Time Series.
# 

# https://www.bis.org/publ/bcbs_wp14.pdf
# 
# https://www.bis.org/ifc/events/ws_micro_macro/nehrebecka_paper.pdf
# 
# https://www.bis.org/bcbs/events/oslo/liebigblo.pdf
# 
# https://www.bundesbank.de/resource/blob/704150/b9fa10a16dfff3c98842581253f6d141/mL/2003-10-01-dkp-01-data.pdf
# 
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5495014/
# 
# https://www.casact.org/pubs/monographs/papers/05-Goldburd-Khare-Tevet.pdf
# 
# https://www.crowe.com/insights/credit-risk-model-validation
# 
# https://www.moodysanalytics.com/-/media/products/Model-Monitoring.pdf
# 
# https://www.finity.com.au/wp-content/uploads/2014/05/07.-Model-monitoring.pdf
# 
# https://www.accenture.com/gb-en/~/media/accenture/conversion%20assets/dotcom/documents/global/pdf/dualpub_7/accenture-credit-risk-model-monitoring.pdf
# 
# 
# 
#  Còn liên quan tới Academic, chúng tôi chỉ tham khảo các Bài báo quốc tế và Giao trình chuyên nghành về Toán và Kinh tế Lượng. Thêm vào đó, quan điểm của chúng tôi là chỉ chọn lựa và tham khảo các cách tiếp cận đã được thừa nhận, sử dụng rộng rãi như các Giao trinh trong trường ĐH Hàng đầu được xuất bản bởi các Nhà Xuất bản Uy tin trên thế giới như John Wiley & Son, etc và Tạp Trí Khoa Học Hàng đầu, chẳng hạn như Tạp chí Computational Economics,  Journal of International Economics, etc.
# 
# Trên cơ sở đó, chúng tôi thấy rằng hai tài liệu sau của Nhóm tác giả tại Trung Tâm Nghiên Cứu Chung (Joint Research Center), trực thuộc Ủy Ban Châu Âu và Khoa Khoa Học Máy Tính, thuộc Đại Học Manitoba, Canada, như một nền tảng cho việc thực hiện dự án Phân tích Độ Nhạy của Mô hình Logistic. 
# 
# 1. Saltelli, A.; Ratto, M.; Andres, T.; Campolongo, F.; Cariboni, J.; Gatelli, D.; Saisana, M.; Tarantola, S. (2008). Global Sensitivity Analysis: The Primer. John Wiley & Sons.
# 
# Link tải: 
# 
# 
# http://www.andreasaltelli.eu/file/repository/A_Saltelli_Marco_Ratto_Terry_Andres_Francesca_Campolongo_Jessica_Cariboni_Debora_Gatelli_Michaela_Saisana_Stefano_Tarantola_Global_Sensitivity_Analysis_The_Primer_Wiley_Interscience_2008_.pdf
# 
# 
# 2. Saltelli, A.; Ratto, M.; Campolongo, F.; Cariboni, J.; Gatelli, D.; Saisana, M.; Tarantola, S. (2008). Sensitivity Analysis In Practice: A Guide to Scientist Models.
# 
# Link tải
# 
# http://www.andreasaltelli.eu/file/repository/SALTELLI_2004_Sensitivity_Analysis_in_Practice.pdf
# 
# Lý do chính của việc lựa chọn này là theo quan điểm của chúng tôi đó là định nghĩa của Nhóm tác giả này có tính chât bao quát và chung nhất cho các khái niệm quan điểm khác nhau về vấn đề Phân Tích Độ Nhạy (Sensitivity Analysis) của một Mô Hình. Thêm vào nữa, Nhóm tác giả cũng sử dụng một loạt các phương pháp phổ biến nhất trong Phân Tích Độ Nhạy (Sensitivity Analysis) của một Mô Hình và lượng hóa chỉ tiêu này.
# 
# Đặc biệt, tác giả Marco Ratto, bản thân người làm dự án này đã được theo học hai khóa học về DYNARE (công cụ phân tích Mô Hình DSGE) tại Paris, Pháp (2017) và Tại Ispra, Italy (2019). Chính hai giáo trình trên chúng tôi được tác giả Marco Ratto giới thiệu tham khảo.
# 
# 
# Bên cạnh đó, chúng tôi chọn những Các bài báo quốc tế đăng ở Tạp chí ở dạng Frontier
# 
# Của tác giả Marco Ratto trên tập chí Computational Economics
# 1. Analysing DSGE Models with Global Sensitivity Analysis. 
# https://link.springer.com/article/10.1007/s10614-007-9110-6
# 
# Bài nghiên Cứu của Nhóm tác giả Ngân hàng Trung Ưowng Thụy Điển (Riskbank), nơi chúng tôi đã có cơ hội làm việc với Nhóm này, trên Tạp chí Journal of International Economics
# 2. Bayesian estimation of an open economy DSGE model with incomplete pass-through. Adolfson
# https://www.sciencedirect.com/science/article/pii/S0022199607000219
# 
# 
# 
# 
# Do đó, trong quá trình thực hiện, chúng tôi xen kẽ kêt hợp cả hai hướng tiếp cận của academic và industry với nhau. Trước tiên chúng ta hay cùng nhau hiểu theo hương tiếp cận academic một chút.
# 
# $\color{blue}{\textbf{1. Khái niệm Phân Tích Độ Nhạy}}$
# 
# $\color{blue}{\textbf{1.1 Theo góc độ hàm Toán học}}$
# 
# Khái niệm Phân Tích Độ Nhạy (Sensitivity Analysis) là một khái niệm rộng. Theo đó, dưới góc độ các hàm toán học, định nghĩa về Phân Tích Độ Nhạy (Sensitivity Analysis), trong Giáo Trình: "Global Sensitivity Analysis: The Primer" của Nhóm tác giả Châu Âu và Canada nêu ra như sau:
# 
# "Phân Tích Độ Nhạy là việc nghiên cứu sự bất ổn/biến động trong đầu ra của một mô hình toán hoặc hệ thống (số hoặc khác) có thể được chia và phân phối cho các nguồn khác nhau của sự bất ổn định trong những yếu tố đầu vào của nó".
# 
# $$\textbf{"Sensitivity analysis is the study of how the uncertainty in the output}$$
# $$\textbf{of a mathematical model or system (numerical or otherwise) can be}$$
# $$\textbf{divided and allocated to different sources of uncertainty in its inputs}"$$
# 
# Như vậy, chúng ta có hiểu vấn đề về khái niệm Phân tích Độ Nhạy (Sensitivity Analysis) của một Mô Hình toán như sau: là quá trình thử nhiệm/kiểm tra sự phản ứng/biến động/bất ổn trong kết quả đầu ra của một mô hình toán (the uncertainty in the output of a mathematical model) với lại các giả định/giả thuyết/trường hợp bất ổn (uncertainty) khác nhau của các yếu tố đầu vào (different sources of uncertainty in its inputs). 
# 
# Hay một cách ngắn gọn hơn, Phân tích Độ Nhạy (Sensitivity Analysis) của một Mô Hình toán là quá trình nghiên cứu sự thay đổi, biến động của kết quả đầu ra của một Mô Hình toán khi chúng ta  các yếu tố đầu vào của nó.
# 
# 
# Cụ thể hơn, giả sử chúng ta có một hàm toán học không có lỗi hay sai số như dưới đây:
# 
# $$Y=\sum_{i=1}^{r}\omega_{i}Z_{i} \  \ (1.3)$$ 
# 
# Trong hàm toán trên, chúng ta thấy các yếu tố đầu vào bao gồm 
# $X=(\omega_{i},\omega_{i},...,\omega_{r},Z_{1}, Z_{2},...,Z_{r})$. Để đơn giản, chúng ta sẽ giả định các hệ số $\omega_{i}$ là cố định, chỉ có các yếu tố $Z_{i}$ là các biến thay đổi. Bây giờ chúng ta giả định là các yếu tố đầu vào $Z_{i}$ cùng phân phối thay đổi theo một quy luật là Phân phối thường (Normal distribution) như dưới đây:
# 
# $$Z_{i}  \thicksim N(0,\sigma_{Z_{i}}), \ \& \ i=(1,2,..r)$$
# 
# Khi đã biết Hàm phân phối của các biến đầu vào $Z_{i}$ như ở trên, chúng ta sẽ sử dụng Phương pháp  Monte Carlo để lấy mẫu cho các $Z_{i}$, giả sử 1000 Mẫu chẳng hạn. Dựa vào 1000 mẫu này, lắp lại vào Mô Hình Toán (1.3), chúng ta có thể lấy được 1000 Mẫu kết quả đầu ra $Y$ tương ứng. Đến đây chúng ta có thể tiến hành phân tích được sự biến động của Biến đầu ra cũng sẽ theo một Phân Phối thường. Tại sao? Bởi vì ở trên chúng ta đã giả định cac yếu tố đầu vào $Z_{i}$ theo một quy Phân phối thường. Cụ thể hơn, Phân phối thường của biến đầu ra $Y$ sẽ có giá trị Trung bình và Sai số chuẩn như ở công thức dưới đây:
# 
# ![Mean%20Var.png](attachment:Mean%20Var.png)
# 
# 
# 
# Dựa trên những thông tin trên, chúng ta có thể tiến hành phân tích độ Nhạy của Hàm toán học (1.3). Vậy câu hỏi đặt ra là: Phương pháp phân tích độ nhạy là gì?
# 
# ![SA%20Methods.png](attachment:SA%20Methods.png)
# 
# Đề cập về phương pháp Phân tích độ nhạy cho các Hàm Toán học, trong Giao trình này Nhóm tác giả đề cập tới nhiều Phương pháp, nhưng với cách tiếp cận đạo hàm (derivative) là được sử dụng phổ biến hơn cả. Cụ thể, giáo trình ghi tại Trang 11:

# Tuy nhiên, trước tiên chúng ta hãy phân tích độ nhạy của biến đầu ra $Y$ bằng phương pháp đồ thị Scatter plot với các biến đầu vào $Z_{i}$ như hình dưới đây
# 
# ![SA_Scatter.png](attachment:SA_Scatter.png)
# 
# 
# Dựa trên đồ thị trên chúng ta dễ dàng nhận thấy yếu tố đầu ra $Y$ rất nhạy cảm với biến đầu vào $Z_{4}$  và kém nhạy với biến đầu vào $Z_{1}$ bởi vì quan hệ giữa $Y$ và $Z_{4}$ phân bổ rộng hơn so với quan hệ giữa $Y$ và $Z_{1}$ (chỉ quanh quẩn ở tọa độ 0).

# Mô tả khái niệm theo Lược đồ,
# 
#  
# 
# Nguồn: https://en.wikipedia.org/wiki/Sensitivity_analysis
# 
# 
# Đồng thời, để thực hiện Phân Tích Độ Nhạy cho các hàm toán học như trong Giáo Trình trên, có thể sử dụng Thư viện như SaLib 
# 
# https://salib.readthedocs.io/en/latest/basics.html#what-is-salib

# $\color{blue}{\textbf{1.2 Theo góc độ Kinh Tế Lượng}}$
# 
# Các mô hình Kinh tế lượng cũng là một dạng hàm Toán học. Do đó, theo quan điểm cá nhân của chúng tôi, khi phân tích độ nhạy của một mô hình kinh tế lượng bất kỳ, cụ thể trong dự án này là phân tích độ nhạy của Mô Hình Logistic, thì khái niệm Phân tích độ nhạy, phương pháp phân tích độ Nhạy cũng sẽ giống với khái niệm Phân tích Độ Nhạy (Sensitive Analysis), và phương pháp phân tích độ nhạy của các Hàm Toán học, như trong hai Giao trình của các tác giả Châu Âu chúng tôi nêu ra ở trên.
#  
# Trước khi đi xâu vào vấn đề, điều quan trọng trước tiên chúng ta phải nhắc lại và hiểu được Mô hình Logistic, để thấy được các nội dung như, đâu là đầu ra, đâu là đầu vào của Mô hình Logistic. Để từ đó, chúng ta sẽ đưa ra các phương pháp, tiếp cận để phân tích độ nhạy của Mô hình Logistic
# 
# 
# Trên cở sở Mô Hình Logistic nêu ra ở trên, chúng tôi xác định các yếu tố để phân tích Độ Nhạy của Mô Hình như sau:
# 
# 1. Yếu tố đầu ra: Chỉ số Log Odd, Likelihood, Gía trị dự báo
# 
# 2. Yếu tố đầu vào: Các hệ số của Mô Hình, Các Biến giải thích, và Phần dư (Lỗi và sai sót)
# 
# Trên cơ sở đó, kết hợp với khái niệm về Phân tích độ nhạy, chúng tôi sẽ tiến hành Phân tích Độ Nhạy của Mô Hình Logistic bằng cách thử môt loạt các thay đổi Đầu Vào của Mô hình Logistic như: Các Biến giải thích, và Phần dư (Lỗi và sai sót), để xem các yếu tố Đẩu Ra của Mô hình Logistic như: Chỉ số Log Odd, Likelihood, Gía trị dự báo, sẽ thay đổi như thê nào
# 
# 
# 
# Tóm lại, Nhìn chung, Góc độ Kinh tế lượng thì định nghĩa về Phân Tích Độ Nhạy (Sentitive Analysis) không khác xa nhiều đối với định nghĩa về Phân Tích Độ Nhạy của các hàm Toán học trên.Theo đó, chúng ta có thể hiểu Phân Tích Độ Nhạy (Sentitive Analysis) của một Mô Hình Kinh tế Lượng/Thuật Toán nói chung là xem xem sự phản ứng của Mô hình sẽ như thế nào đối với một tình huống bất ổn (uncertainty) được giả định xảy ra. Cụ thể, trong dự án này, chúng ta sẽ tiến hành phân tích Độ Nhạy/Phản ứng của Mô Hình Logistic trong bốn tình huống bất ổn (uncertainty) giả định xảy ra trong các khía cạnh dưới đây:
# 
# 1. $\textbf{Độ Nhạy của Mô Hình Logistic với từng biến giải thích}$: Khi một biến giải thích trong mô hình biến động, nó sẽ tác động như nào tới Mô Hình.
# 
# 2. $\textbf{Độ Nhạy của Mô Hình Logistic với số biến giải thích}$: Chúng ta sẽ kiểm tra xem số biến giải thích sẽ tác động như thế nào tới Mô hình. Cụ thể, số biến tăng/giảm sẽ ảnh hưởng như nào tới Mô Hình.
# 
# 3. $\textbf{Độ Nhạy của Mô Hình Logistic với số quan sát}$: Chúng ta sẽ kiểm tra xem, số quan sát tăng/giảm sẽ ảnh hưởng thế nào tới Mô hình. Chúng ta cần thu thập bao nhiêu quan sát là đủ để ước lượng Mô Hình?
# 
# 4. $\textbf{Độ Nhạy của Mô Hình Logistic với Độ Nhạy của các Mô hình khác}$:  Chúng ta sẽ xem xem với cùng một số biến giải thích và số quan sát như nhau, thì Độ Nhạy của Mô Hình Logistic như thế nào so với các Mô Hình khác.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Dưới đây là Bảng Nội dung phân tích
# 
# $\underline{\color{blue}{\textbf{V. Bảng Nội Dung Thực Hiện Dự Án}}}$
# 
#  $$\Large \color{blue}{\textbf{Phần I: Chuẩn Bị Cấu Hình Programming}}$$
# 
#  1. <a href='#Lib'>Lib</a>  
#  
#  
#  2. <a href='#DataImport'> Nhập Dữ Liệu </a>  
#  
#  
#  $$\Large \color{blue}{\textbf{Phần II: Chuẩn Bị Dữ Liệu}}$$
#  
#  3.  <a href='#EDA'>Khai phá dữ liệu (EDA) </a>   
#  
#  3.1. <a href='#EDA_1'>Chọn Mẫu </a>  
#  
#  3.2. <a href='#EDA_2'>Kiểm tra kích cỡ </a>  
#  
#  3.3. <a href='#EDA_3'>Kiểm tra Biến </a>
#  
#   3.4. <a href='#EDA_4'>Kiểm tra Dạng Dữ Liệu </a> 
#  
#  3.5. <a href='#EDA_5'>Kiểm tra Thiếu Biến </a> 
#  
#  3.6 <a href='#EDA_6'>Thống Kê Mô Tả </a> 
#  
#  3.7 <a href='#EDA_7'>Các biến phân loại </a> 
#  
#     3.7.1 <a href='#EDA_71'>EDUCATION </a> 
#     
#     3.7.2 <a href='#EDA_72'>MARRIAGE </a> 
#     
#   
#  
#  4. <a href='#DataPre_1'>Chuẩn bị dữ liệu </a> 
#  
#  4.1 <a href='#DataPre_1'>Dữ liệu đầu vào </a> 
#  
#      4.1.1  <a href='#DataPre_11'>Chọn Dữ liệu đầu vào </a> 
#  
#      4.1.2 <a href='#EDA_9'>Dữ liệu dạng Pandas </a> 
#      
#      4.1.3 <a href='#EDA_8'>Đồng bộ hóa đơn vị </a> 
#  
#  4.2 <a href='#DataPre_2'>Dữ liệu đầu ra </a> 
#  
#      4.2.1 <a href='#DataPre_21'>Chọn Dữ liệu đầu ra </a> 
#      
#      4.2.2 <a href='#DataPre_22'>Phân bổ Dữ liệu đầu ra </a> 
#      
#  4.3 <a href='#DataPre_33'>Mối quan hệ biến đầu vào và đầu ra </a>
#      
#   4.4 <a href='#DataPre_3'>Phân tách dữ liệu </a> 
#      
#  $$\Large \color{blue}{\textbf{Phần III: Phát Triển Mô Hình}}$$
#  
#  5. <a href='#Train'>Đào tạo Mô Hình </a> 
#  
#     5.1 <a href='#Train_10'>Xác lập cấu hình và khớp dữ liệu </a> 
#     
#     5.2 <a href='#Train_1'>Gía trị fitted đầu ra </a> 
#  
#   $$\Large \color{blue}{\textbf{Phần IV: Đánh Gía và Phân Tích Độ Nhạy Của Mô Hình}}$$
#     
#  $$\Large \color{blue}{\textbf{In-Sample Sentivitity Analysis and Validation }}$$
#  
#  
#  <a href='#Train_11'>Phân Tích nghĩa thóng kê của biến giải thích</a> 
#  
#  <a href='#Valid_102'>Phân tích Đồ thị Scatter </a> 
#  
#  <a href='#Valid_101'>Hiệu Ứng Biên (Phương pháp đạo hàm) </a> 
#     
#  <a href='#Valid_1022'>Variance inflation factor</a> 
#  
#  <a href='#Valid_101'>Kiểm Định Wald </a> 
#  
#   <a href='#Valid_102'>Vai Trò Các Biến Giải Thích </a> 
#  
#  <a href='#Valid_100'>Deviance </a> 
#  
#  <a href='#Valid_1012'>Biến Động Gía Trị Likelihood </a> 
#  
#  <a href='#Valid_1013'>Biến Động Tỷ số Thống kê Likelihood chi-squared</a> 
#  
#  <a href='#Valid_1014'>Biến Động Chỉ Số Pseudo-R-squared</a>
#  
#  <a href='#Valid_1015'>Sự phức tạp của Mô Hình</a>
#      
#  <a href='#Valid_11'>Phân Tích ANOVA( Analysis Of Variance) </a> 
#     
#  <a href='#Valid_12'>Độ Nhạy Của Mô Hình Với Số Biến Giải Thích </a>
#     
#  <a href='#Valid_13'>Độ Nhạy Của Mô Hình Với Số Quan Sát </a> 
#     
#  <a href='#Valid_133'>Deviance Residual  </a> 
#  
#  <a href='#Valid_136'>Log Loss </a> 
#  
#  <a href='#Valid_134'>Working Residuals </a> 
#  
#  <a href='#Valid_135'>Cook’s Distance </a> 
#    
#  <a href='#Valid_1399'>Thống Kê Kolmogorov–Smirnov (KS) </a> 
#    
#  <a href='#Valid_134'>Ma Trận Confusion  </a> 
#    
#  <a href='#Valid_135'>Chỉ Tiêu AUROC </a> 
#  
#  <a href='#Valid_1350'>Bootstrap Analysis AUROC </a> 
#  
#  <a href='#Valid_1351'>Khoảng Tin Cậy Cho AUROC </a> 
#    
#  <a href='#Valid_136'>Hệ Số Gini (Accuracy Ratio AR) </a> 
#  
#  <a href='#Valid_1367'>Bootstrap for Gini (Accuracy Ratio AR) </a> 
#  
#  <a href='#in_sam45'>In-sample Prediction Error </a>  
#    
#  <a href='#in_sam18'>CAP – Cumulative Accuracy Profile </a> 
#  
#  <a href='#in_sample70'>In-Sample Discriminatory Power Của Mô Hình Logistic </a> 
#  
#   <a href='#in_sample09'>Lorenz Curve</a> 
#   
#   <a href='#in_sample91'>Điểm Brier và Calibration Plots</a> 
#   
#   <a href='#insmap1791'>The Information Entropy </a>   
#   
#   <a href='#insmap179'>Precision-Recall Curve </a>  
#  
#   <a href='#in_sample79'>Đường Cong Kiểm Định (Validation Curve)</a> 
#   
#   <a href='#in_sample793'>Xác Xuất Vỡ Nợ (PD) Và Tỷ Lệ Duyệt Khoản Vay</a> 

#     
#  $$\Large \color{blue}{\textbf{Phần V: Giam Sát Hoạt Động Của Mô Hình}}$$
#  
#  $$\Large \color{blue}{\textbf{Model Monitoring}}$$
#     
#  $$\Large \color{blue}{\textbf{Out-Of-Sample Sentivitity Analysis and Validation}}$$
#  
# Phần này chúng ta sẽ tiến hành Giam sát hoạt động của Mô Hình, cụ thể chúng ta sẽ theo hướng tiếp cận của Industry như của Moody hay Finity của Úc, etc.. Nhưng nhìn chung chỉ tiêu để giám sát Mô Hình đó là sử dụng Phần diện tích dưới đường cong ROC. Theo đó, Mô hình được cho là hiệu quả nếu phần diện tích này càng về sát với 1.
# 
#  <a href='#out_of90'>Out-Of-Sample Predictor Error </a>    
#  
#  <a href='#out_of9'>Out-Of-Sample Confusion Matrix </a>    
#  
#  <a href='#out_of1'>Out-Of-Sample AU-ROC </a>    
#  
#  <a href='#out_of191'>Bootstrap AU-ROC </a>   
#  
#  <a href='#outofSam_1351'>Khoảng Tin Cậy Cho AUROC </a> 
#  
#  <a href='#out_of19'>Hệ Số Gini (Accuracy Ratio AR) </a>  
#  
#  <a href='#out_of191'>Bootstrap for Gini (Accuracy Ratio AR) </a>   
#  
#  <a href='#in_sam18'>CAP – Cumulative Accuracy Profile </a>   
#  
#  <a href='#out_of17'>Discriminatory Power Của Mô Hình Logistic </a> 
#  
#  <a href='#out_of177'>Lorenz Curve Monitoring </a>   
#  
#  <a href='#out_of178'>Điểm Brier and Calibration Curves </a>    
#  
#  <a href='#out_of1799'>The Information Entropy </a>  
#  
#  <a href='#insmap179'>Precision-Recall Curve </a>  
#  
#  <a href='#out_of3'>Sự Ổn Định Của Logistic </a>    
#  
#  <a href='#out_sample793'>Xác Xuất Vỡ Nợ (PD) Và Tỷ Lệ Duyệt Khoản Vay</a>
#  
#  <a href='#Valid_13'>So Sánh Độ Nhạy Của Mô Hình Logistic với các Model khác  </a> 
#  
# 
#  

# $$\Large \color{blue}{\textbf{Phần I: Chuẩn Bị Cấu Hình Programming}}$$
# 
# 
# # <a href='#Lib'>Lib</a>   

# In[1189]:


import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))


# In[611]:


import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))


# In[1201]:


from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


# In[1649]:


import os
import itertools
import math

import scipy.interpolate
import scipy.integrate
from timeit import default_timer as timer
import numpy as np
import pandas as pd
from patsy import dmatrices
from scipy import stats
from pandas import set_option
from pandas.plotting import scatter_matrix
from timeit import default_timer as timer
from sklearn.preprocessing import label_binarize
from math import log2
from scipy.stats import sem

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectFromModel


# In[613]:


#from markdown.extensions.toc import TocExtension


# In[1576]:


import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB, ComplementNB, MultinomialNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import Lasso
from sklearn.linear_model import LassoLars
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import PassiveAggressiveRegressor
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier


# In[1487]:


#from SALib.sample import saltelli
#from SALib.analyze import sobol
from yellowbrick.regressor import CooksDistance
from yellowbrick.regressor import cooks_distance # quick method
from yellowbrick.regressor import PredictionError
from yellowbrick.classifier import ClassPredictionError
from yellowbrick.model_selection import ValidationCurve
from scipy import stats
from statsmodels.stats.api import anova_lm
from sklearn import metrics
from sklearn import model_selection
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.calibration import CalibratedClassifierCV, calibration_curve

from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import (brier_score_loss, precision_score, recall_score)
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from yellowbrick.classifier import DiscriminationThreshold
#from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import auc
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from statsmodels.stats.outliers_influence import variance_inflation_factor
from pyitlib import discrete_random_variable as drv


# In[616]:


from pickle import dump
from pickle import load
Purple= '\033[95m'
Cyan= '\033[96m'
Darkcyan= '\033[36m'
Blue = '\033[94m'
Green = '\033[92m'
Yellow = '\033[93m'
Red = '\033[91m'
Bold = "\033[1m"
Reset = "\033[0;0m"
Underline= '\033[4m'
End = '\033[0m'
from pprint import pprint


# # <a href='#DataImport'> Nhập Dữ Liệu </a>  

# In[617]:


print(Bold + Blue + 'Thư mục làm việc hiện tại của bạn:' + End)
print(os.getcwd())


# In[618]:


data= pd.read_csv('default of credit card clients.csv',header=1)


# $$\Large \color{blue}{\textbf{Phần II: Chuẩn Bị Dữ Liệu}}$$
# 
# # <a href='#EDA'>Khai phá dữ liệu (EDA) </a>     

# ## <a href='#EDA_1'>Chọn Mẫu </a>     

# In[619]:


data.head(5)


# ## <a href='#EDA_2'>Kiểm tra kích cỡ </a>  

# In[620]:


print("Số quan sát: %d. Số Biến: %d"%(data.shape))


# ## <a href='#EDA_3'>Kiểm tra Biến </a>  

# In[621]:


print(Bold+"Tên %d Biến trong Dữ Liệu:"%(len(data.columns))+End)
print(data.columns)


# ## <a href='#EDA_4'>Kiểm tra Dạng Dữ Liệu </a>  

# In[622]:


print(Bold+"Dạng Dữ liệu của %d Biến:"%(len(data.columns))+End)
print(data.dtypes)


# ## <a href='#EDA_5'>Kiểm tra Thiếu Biến </a> 

# In[623]:


print(Bold+"Số giá bị thiếu trong %d Biến"%len(data.columns)+End)
print(data.isnull().sum())


# ## <a href='#EDA_6'>Thống Kê Mô Tả </a> 

# In[624]:


print(Bold+"Thống Kê Mô Tả:"+End)
print(data.describe())


# ## <a href='#EDA_7'>Các biến phân loại </a> 

# In[14]:


print(Bold+"Phân loại của Biến 'SEX':"+End)
print(data["SEX"].unique())
print(Bold+"Phân loại của Biến 'EDUCATION':"+End)
print(data["EDUCATION"].unique())
print(Bold+"Phân loại của Biến 'MARRIAGE':"+End)
print(data["MARRIAGE"].unique())


# SEX: Gender (1=male, 2=female)
# 
# EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
# 
# MARRIAGE: Marital status (1=married, 2=single, 3=others)

# ### <a href='#EDA_71'>EDUCATION </a> 

# In[33]:


print(Bold+"Các phân loại của Biến 'EDUCATION':"+End)
print(data["EDUCATION"].unique())
print(Bold+"Số phân loại của Biến 'EDUCATION':"+End)
print(data["EDUCATION"].value_counts())


# EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)

# In[34]:


data[data["EDUCATION"]==0]=4
data[data["EDUCATION"]==5]=4
data[data["EDUCATION"]==6]=4


# In[35]:


print(data["EDUCATION"].unique())
print(Bold+"Phân loại của Biến 'MARRIAGE':"+End)
print(data["EDUCATION"].value_counts())


# EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others)

# ### <a href='#EDA_72'>MARRIAGE </a> 

# In[36]:


print(Bold+"Các phân loại của Biến 'MARRIAGE':"+End)
print(data["MARRIAGE"].unique())
print(Bold+"Số Phân loại của Biến 'MARRIAGE':"+End)
print(data["MARRIAGE"].value_counts())


# In[ ]:


data[data["MARRIAGE"]==0]=4
data[data["MARRIAGE"]==6]=4


# # <a href='#DataPre_1'>Chuẩn bị dữ liệu </a> 

# ## <a href='#DataPre_1'>Dữ liệu đầu vào </a> 

# ### <a href='#DataPre_11'>Chọn Dữ liệu đầu vào </a> 

# In[625]:


X=data.iloc[:,1:24]
X.columns


# In[626]:


X.head(5)


# ### <a href='#EDA_8'>Đồng bộ hóa đơn vị </a> 

# In[627]:


standardized_x = preprocessing.scale(X)
standardized_x[1:5]


# ### <a href='#EDA_9'>Dữ liệu dạng Pandas </a> 

# In[628]:


standardized_X=pd.DataFrame(data=standardized_x,
                           columns=X.columns)
standardized_X.head()


# In[629]:


standardized_X.shape


# ## <a href='#DataPre_2'>Dữ liệu đầu ra </a> 

# ### <a href='#DataPre_21'>Chọn Dữ liệu đầu ra </a> 

# In[630]:


Y=data["default payment next month"]
Y.head(5)


# ### <a href='#DataPre_22'>Phân bổ Dữ liệu đầu ra </a> 

# In[700]:


plt.figure(figsize=(8, 5))
ax = sns.countplot(x="default payment next month", data=data)
plt.title("Phân Bổ Giữa Các Trường Hợp Không Xảy Ra Vỡ Nợ và Xảy Ra Vỡ Nợ",fontsize=14,
          fontweight='bold',color='g')
plt.show()


# Có thể thấy sự mất cân đối cực lớn giữa hai giá trị đầu ra. Đây cũng là một trong những vấn đề phổ biến trong các bài toán thực tế. Do đó, sử lý dữ liệu mất cân đối là một trong những bước QUAN TRỌNG đầu tiên, trong đào tạo và ước lượng Mô Hình phân tích.

# ## <a href='#DataPre_33'>Mối quan hệ biến đầu vào và đầu ra </a> 

# In[632]:


sns.set()
fig=plt.figure(figsize=(7,5))
plt.scatter(x=standardized_X['LIMIT_BAL'], y=data["default payment next month"]
            , cmap='rainbow')
plt.xlabel('Limited Balance')
plt.ylabel('Default Payment')
plt.show()


# In[24]:


sns.set()
fig=plt.figure(figsize=(12,5))
sns.lmplot(x='LIMIT_BAL',
           y="default payment next month", data=data, logistic=True, y_jitter=.05)


# In[1027]:


data.columns


# In[ ]:





# In[1028]:


LIMIT_BAL = sns.regplot(x= 'LIMIT_BAL', y= 'default payment next month',
                        data= data, logistic= True).set_title("LIMIT_BAL Log Odds Linear Plot")


#gpa = sns.regplot(x= 'gpa', y= 'admit', data= df, logistic= True).set_title("GPA Log Odds Linear Plot")


# In[ ]:


gre = sns.regplot(x= 'gre', y= 'admit', data= df, logistic= True).set_title("GRE Log Odds Linear Plot")
gre.figure.savefig("gre log lin.png")

gpa = sns.regplot(x= 'gpa', y= 'admit', data= df, logistic= True).set_title("GPA Log Odds Linear Plot")
gpa.figure.savefig("gpa log lin.png")


# ## <a href='#DataPre_3'>Phân tách dữ liệu </a> 
# 
# Chúng ta sẽ phân tách dữ liệu thành hai phần: Phần Train và phần Validation/Monitoring. Mô hình sẽ được đào tạo trên phần Train, sau đó sẽ kiểm tra hoạt động trên phần Validation/Monitoring. Trong các bài thực tế, phân tách dữ liệu BẮT BUỘC phải thực hiện theo phân tách NGẪU NHIÊN. Tuy nhiên, trong bài toán này chúng ta phân tách dữ liệu bằng tay. Tỷ lệ phân tách sẽ là 70/30.
# 
# ![SplitingDat.png](attachment:SplitingDat.png)
# 
# Để có được tỷ lệ phân chia 70/30, thì chúng ta cần xác định được điểm phân chia. Cụ thể, chúng ta sẽ lấy 21000 quan sát đầu tiên trong bộ dữ liệu để đào tạo mô hình, và số còn lại là để kiểm định mô hình như sau

# In[633]:


split_cuttoff=round(0.7*len(X),)
print("Điểm phân chia: %d"%split_cuttoff)


# In[634]:


X_train = standardized_X[:split_cuttoff]
X_valid = standardized_X[split_cuttoff:]


# In[635]:


Y_train = Y[:split_cuttoff]
Y_valid = Y[split_cuttoff:]


#  $$\Large \color{blue}{\textbf{Phần III: Phát Triển Mô Hình}}$$
# 
# # <a href='#Train'>Đào tạo Mô Hình </a> 

# ## <a href='#Train_10'>Xác lập cấu hình và khớp dữ liệu </a> 

# In[636]:


Logit_Mod1 = sm.Logit(Y_train, X_train)
#result_Logit1 = Logit_Mod1.fit(method='newton')# Phương pháp tìm điểm Log likelood lớn nhất là newton
result_Logit1=Logit_Mod1.fit_regularized()
print(result_Logit1.summary2())


# ## <a href='#Train_1'>Gía trị fitted đầu ra (log odds) </a> 

# In[638]:


fitted_LogOdd=result_Logit1.fittedvalues
sns.set()
fig=plt.figure(figsize=(12,5))
plt.plot(fitted_LogOdd,LineWidth=1)
plt.autoscale(enable=True,axis='both',tight=True)
#plt.grid(linestyle=':',which='both',linewidth=2)
#fig.suptitle('Gía trị Log odds ('log(\frac{p}{1-p})')', fontsize=15,fontweight='bold')
plt.title('Gía Trị Log Odds Ước Lượng Từ Mô Hình Logistic',
          fontsize=14,fontweight='bold',color='k')
plt.ylabel(r'$Log(\frac{p}{1-p})$',fontsize=12)
plt.xlabel('%d Giá Trị Log Odd Ước Lượng được từ Mô Hình Logistic'%len(fitted_LogOdd),
           fontsize=12,
           fontweight='normal',color='k')


# $$\Large \color{blue}{\textbf{Phần IV: Đánh Gía và Phân Tích Độ Nhạy Của Mô Hình}}$$
#     
#  $$\Large \color{blue}{\textbf{In-Sample Sentivitity Analysis and Validation }}$$
#  
#  Trong phần nội dung này, chúng tôi sẽ tiến hành phân tích Độ nhạy để kiểm định Mô Hình Logistic cho trường hợp $\textbf{In-sample}$. Phần phân tích độ nhạy cho giám sát $\textbf{(monitoring)}$ sẽ được tiến hành ở phần sau $\textbf{Out-Of-Sample}$
# 
# 
# # <a href='#Valid'>Kiểm Định và Phân tích độ nhạy của Mô Hình </a> 
# 
# ## <a href='#Valid'>In-sample Model Validation and Sensitivity Analysis </a> 
# 
# 
# 
# 

# ### <a href='#Train_11'>Phân Tích nghĩa thóng kê của biến giải thích</a>

# In[1012]:


pval=result_Logit1.pvalues
print(Red+Bold+'Tổng số biến giải thích trong Mô Hình Logistic: %d'%len(pval)+End)
print(Red+Bold+'Trong đó, Có:'+End)

selecte_valStat=pval[pval.values<0.05]
print(Bold+ Red+"%d Biến giải thích có ý nghĩa thống kê ở mức 0.05. Đó là:"%len(selecte_valStat)+End)
print(round(selecte_valStat,2))

selecte_val=pval[pval.values>0.1]
print(Bold+ Red+"Và %d Biến giải thích không có ý nghĩa thống kê ở mức 0.1. Đó là:"%len(selecte_val)+End)
print(round(selecte_val,2))


# ### <a href='#Valid_102'>Phân tích Đồ thị Scatter </a> 

# In[639]:


plt.figure(figsize=(15, 40))
for i,col in enumerate(X_train.columns):
    plt.subplot(6,4,i+1)
    plt.scatter(x=X_train[col],y=fitted_LogOdd)
    plt.xlabel(col)
    plt.ylabel('Fitted Log Odds')   


# ### <a href='#Valid_101'>Hiệu Ứng Biên (Phương pháp đạo hàm) </a> 
# 
# Phương pháp này chính là phương pháp Đạo hàm (Derivative). Như đã đề cập ở trên, trong giáo Trình "Global Sensitivity Analysis: The Primer. John Wiley & Sons",mặc dù có những hạn chế riêng, nhưng Nhóm tác giả có nêu ra là phương pháp Đạo hàm được sử dụng phổ biến và khá đơn giản. Cụ thể, trong bài toán này, chúng ta sẽ tính Hiệu ứng biên (Marginal Effects) của Mô Hình Logistic. Cách tính toán chi tiết có thể tham khảo tại các giáo trình về Kinh tế Lượng, đơn cử như "Introductory Econometric: A Modern Approach" của giáo sư Jeffrey M.Wooldridge nổi tiếng trong frequentist econometrics.

# https://dzone.com/articles/sensitivity-of-logistic-regression-on-ccoefficient

# In[1017]:


param_basedSen=result_Logit1.get_margeff()
print(Bold+"Phân tích độ nhạy của Mô Hình bằng Phương Pháp Đạo Hàm Tính Hiệu Ứng Biên:"+End)
round(param_basedSen.summary_frame(),4)


# ### <a href='#Valid_1022'>Variance inflation factor</a> 

# In[1014]:


y_vif, X_vif = dmatrices("LIMIT_BAL ~ SEX+EDUCATION+MARRIAGE+AGE+PAY_0+PAY_2+PAY_3+PAY_4+PAY_5+PAY_6+BILL_AMT1+BILL_AMT2+BILL_AMT3+BILL_AMT4+BILL_AMT5+BILL_AMT6+PAY_AMT1+PAY_AMT2+PAY_AMT3+PAY_AMT4+PAY_AMT5", X_train, return_type='dataframe')
vif_df = pd.DataFrame()
vif_df["Gía Trị VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[1])]
vif_df["Biến Giải Thích"] = X_vif.columns
print(Bold+"Kết Qủa Phân Tích Gía Trị VIF:"+End)
print(vif_df)


# ### <a href='#Valid_101'>Kiểm Định Wald </a> 
# 
# Bạn có thể thay đổi Gỉa thuyết theo ý của bạn, bằng cách thay đổi thông số trong phàn "hypotheses" dưới đây. Chẳng hạn, tôi muốn kiểm định Hệ số ước lượng của biến LIMIT_BAL bằng 0, của biến PAY_4 bằng 1, và của Biến PAY_5 bằng 0, xảy ra cùng một lúc

# In[1130]:


hypotheses='LIMIT_BAL = 0, PAY_4 = 1,PAY_5=0'
wald_test=result_Logit1.wald_test(hypotheses)
print('Kiểm Định giả thuyết:'+hypotheses)
print(wald_test)
#print('Gía grij Thống Kê Chi-2: %.2f. Gía trị xác xuất: %.2f. Degree of Fredoom: %d'%(wald_test))


# ### <a href='#Valid_102'>Vai Trò Các Biến Giải Thích </a> 

# In[1646]:


model_RFC=RandomForestClassifier()
model_RFC.fit(X_train,Y_train)
name_feature=X_train.columns
RFC_feature_importances=model_RFC.feature_importances_
RFC_selection=pd.DataFrame(data={'Feature':name_feature,
                                      'feature_importance':RFC_feature_importances})

RFC_selection=RFC_selection.set_index(['Feature'])
RFC_selection_temp=100*RFC_selection.sort_values('feature_importance',ascending=False)
RFC_selection_temp['cumulative_importance']=np.cumsum(RFC_selection_temp,axis=0)
RFC_select_cum=RFC_selection_temp#1[ETR_select1['cumulative_importance']<99]

fig=plt.figure(figsize=(12,5))
fig.add_subplot(1,2,1)
plt.barh(RFC_selection['feature_importance'].sort_values(ascending=True).index,
         100*RFC_selection['feature_importance'].sort_values(ascending=True))
plt.autoscale(enable=True, axis='both',tight=True)
plt.ylabel('Biến Giải Thích',fontsize=15)
plt.xlabel('Tỷ Lệ Đóng Góp (%)', fontsize=15)
plt.title('Tỷ Lệ Đóng Góp Từng Biến Giải Thích', size = 16)
plt.grid(which='major',linestyle=':',linewidth=0.9)
for i,v in enumerate(round(100*RFC_selection['feature_importance'].sort_values(ascending=True),2)):
           ax.text(v , i-0.15 , str(v), color='blue')

fig.add_subplot(1,2,2)
axisX=range(1,
      len(RFC_select_cum.sort_values('cumulative_importance',ascending=True).cumulative_importance)+1)
plt.plot(list(axisX),
         RFC_select_cum.sort_values('cumulative_importance',ascending=True).cumulative_importance,
       color='r')
plt.xlabel('Số Biến Giải Thích Trong Mô Hình', size = 14); 
plt.ylabel('Tỷ Lệ Đóng Góp Tích Lũy', size = 14)
plt.title('Tỷ Lệ Đóng Góp Tích Lũy Của Các Biến Giải Thích', size = 16)
plt.show()


# ### <a href='#Valid_100'>Deviance </a> 

# In[1104]:


LogModel=[]
FittedGLM_LogModel=[]
NumVar=[]
NamVar=[]
Devi=[]
print(Red+"Bạn Đừng Sốt Ruột. Tôi Đang Tính Toán Mà! "+End)
print(Red+".............. "+End)
start = timer()
for i, colnam in enumerate(X_train.columns):
    #print(i)
    Logit_GLMset = sm.GLM(Y_train,X_train[X_train.columns[0:i+1]],
                      family=sm.families.Binomial())
    Fitted_Logit_GLM=Logit_GLMset.fit()
    #
    FittedGLM_LogModel.append(Fitted_Logit_GLM)
     #.append(result_EsLogit.)
    NumVar.append(i+1)
    LogModel.append(i+1)
    NamVar.append(colnam)
    Devi.append(round(Fitted_Logit_GLM.deviance,2))
GLMestimate_results= pd.DataFrame(data={'Mô Hình':LogModel,
                                        'Số Biến':NumVar,
                                        'Biến Thêm Vào':NamVar,
                                        'Kết Qủa Ước Lượng':FittedGLM_LogModel,
                                       'Deviance':Devi},)
print(Red+"Ok! Tôi đã tính toán xong rồi đấy. Hết %.2f Giây bạn nhé "%(timer() - start))


# In[1111]:


fig = plt.figure(figsize=(10,5))
plt.plot(GLMestimate_results['Deviance'],GLMestimate_results['Biến Thêm Vào'],
        color='k')
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Biến Động Gía Trị Deviance Của Mô Hình Logistic',
          fontsize=14,fontweight='bold')
plt.ylabel('Biến Giải Thích Thêm/Bớt', fontsize=11)
plt.xlabel('Gía Trị Deviance', fontsize=11)
plt.show()


# ###  <a href='#Valid_11'>Phân Tích ANOVA( Analysis Of Variance) </a> 
# https://www.casact.org/pubs/monographs/papers/05-Goldburd-Khare-Tevet.pdf
# 
# Phân tích ANOVA được thực hiện dễ dàng trong R, khi sử dụng hàm anova.glm()
# 
# https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/anova.glm
# 
# Tuy nhiên, trong Python không có hàm này, do đó, trước tiên, chúng tôi tiến hành xây dựng Hàm, Phuong_ANOVA, cho tính toán phân tích của chúng tôi giành cho mục đích phân tích ANOVA như dưới đây.

# In[1090]:


def Phuong_ANOVA(small_model, big_model):
    """
    Hàm Phuong_ANOVA này dùng để phân tích ANOVA. Khi bạn khai báo hai Mô hình cần so sánh,
    Kết quả trả về sau khi phân tích ANOVA là Gía trị F thống kê và Gía trị xác xuất
    tương ứng của nó 
    """
    addtl_params = big_model.df_model - small_model.df_model
    f_stat = (small_model.deviance - big_model.deviance) / (addtl_params * big_model.scale)
    df_numerator = addtl_params
    df_denom = (big_model.fittedvalues.shape[0] - big_model.df_model)
    p_value = stats.f.sf(f_stat, df_numerator, df_denom)
    return (f_stat, p_value)


# In[1098]:


CompetModel=[]
PariModel=[]
NumVar=[]
NamVar=[]
F_val=[]
P_val=[]
print("Bạn Đừng Sốt Ruột. Tôi Đang Phân Tích ANOVA Bằng Hàm Phuong_ANOVA Mà! ")
print("Sẽ Xong Nhanh Thôi Bạn À ")
print(".............. ")
start = timer()
for i, colnam in enumerate(X_train.columns):
    if i+1==23: 
        break  
    else:
        f_stat, p_val=Phuong_ANOVA(GLMestimate_results.at[i,'Kết Qủa Ước Lượng'], 
                            GLMestimate_results.at[i+1,'Kết Qủa Ước Lượng'])
        CompetModel.append(i+1)
        PariModel.append([i+1,i+2])
        NumVar.append(i+1)
        NamVar.append(colnam)
        F_val.append(round(f_stat,2))
        P_val.append(round(p_val,2))
print("Đấy thấy chưa! Tôi đã Phân Tích ANOVA xong rồi đấy. Hết có %.2f Giây Thôi bạn nhé "%(timer() - start))
print("Kết quả phân tích ANOVA Tôi in ra ở dưới đây bạn nhé: ")
ANOVA_results= pd.DataFrame(data={'Mô Hình':CompetModel,
                                   'Số Biến':NumVar,
                                   'Biến Thêm Vào':NamVar,
                                   'Cặp So Sánh':PariModel,
                                    'F-Stats':F_val,
                                    'Prob':P_val},)  
pprint(ANOVA_results)


# ### <a href='#Valid_1012'>Biến Động Gía Trị Likelihood </a> 
# 
# Trong phần này, để thấy thêm được vai trò tác động của từng biến giải thích lên kết quả đầu ra của Mô Hình Logistic, chúng tôi tiến hành cố định hệ số của mỗi biến và tiến hành ước lượng các hệ số còn lại trong mô hình dựa trên cùng một bộ dữ liệu. Sau đó, chúng tôi tiến hành Phân tích độ Nhạy của Mô Hình này dựa trên kết quả đầu ra là Likelihood.

# In[1112]:


Model=[]
Fitted_LogMod=[]
Var_num=[]
var_nam=[]
AIC=[]
BIC=[]
LLNull=[]
Loglike=[]
LR=[]
LR_Pval=[]
pseudo_R2=[]
Deviance_resid=[]
print("Xin vui lòng đợi tôi tý nhé.....")
for i, colnam in enumerate(X_train.columns):
    #print(i)
    Logit_Set = sm.Logit(Y_train,X_train[X_train.columns[0:i+1]])
    result_EsLogit=Logit_Set.fit_regularized()
    #
    Fitted_LogMod.append(result_EsLogit)
    AIC.append(result_EsLogit.aic)
    BIC.append(result_EsLogit.bic)
    #.append(result_EsLogit.)
    LLNull.append(result_EsLogit.llnull)
    Loglike.append(result_EsLogit.llf)
    LR.append(result_EsLogit.llr)
    LR_Pval.append(result_EsLogit.llr_pvalue)
    pseudo_R2.append(result_EsLogit.prsquared)
    Deviance_resid.append(result_EsLogit.resid_dev)
    Var_num.append(i+1)
    Model.append(i+1)
    var_nam.append(colnam)
estimate_results= pd.DataFrame(data={'Mô Hình':Model,
                                     'Kết Qủa Ước Lượng':Fitted_LogMod,
                              'Số Biến':Var_num,
                                     'Tên Biến':var_nam,
                                     'AIC':AIC,
                                     'BIC':BIC,
                                     'Log Likehood không biến':LLNull,
                                     'Log Likehood hàm có biến':Loglike,
                                    'Gía trị LR':LR,
                                     'pseudo-R-squared':pseudo_R2,
                                    # 'Deviance residuals':Deviance_resid
                                    'Gía trị LR_Pval':LR_Pval
                                    },)


# In[1113]:


estimate_results.columns


# In[1122]:


fig = plt.figure(figsize=(10,5))
#sns.barplot(estimate_results['Log Likehood hàm có biến'],
 #               estimate_results['Tên Biến'],orient='h')
plt.plot(estimate_results['Log Likehood hàm có biến'],
                estimate_results['Tên Biến'])
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Biến Động Gía Trị Log Likehihood Của Mô Hình Logistic',
          fontsize=14,fontweight='bold')
plt.ylabel('Biến Giải Thích Thêm/Bớt', fontsize=11)
plt.xlabel('Gía Trị Log Likelihood', fontsize=11)
plt.show()


# ### <a href='#Valid_1013'>Biến Động Tỷ số Thống kê Likelihood chi-squared</a> 
# 
# Câu hỏi đặt ra trong tình huống phân tích độ nhạy trong tình huống này là, việc thêm các biến giải thích lần lượt vào Mô Hình Logistic có tác động làm tăng Tỷ số Thống Kê Likelihood chi-squared. Lưu ý rằng, một sự tăng của chỉ số này là tín hiệu tốt nói rằng khả năng Mô Hình ước lượng khớp với dữ liệu thực tế gia tăng. Ngược lại, nếu việc thêm một biến mà làm suy giảm chỉ LR Chi-Squared nói lên rằng việc biến thêm đó làm xấu đi khả năng Mô Hình diễn tả trùng sát với dữ liệu thực. Để thực hiện điều này, chúng tôi xuất phát từ việc Mô Hình Logistic chỉ bào gồm một biến, sau đó, lần lượt các biến tiếp theo được thêm vào Mô Hình. Theo đó, chúng tôi tiến hành ước lượng 23 Mô Hình Logistic với Specification khác nhau. Cuối cùng chúng tôi so sánh chỉ số LR Chi-squared của 23 Mô Hình Logistic với nhau để thấy được Độ Nhạy của Mô Hình Logistic với việc thêm/bớt biến giải thích trong Mô Hình.
# 
# 

# In[32]:


fig = plt.figure(figsize=(10,5))
plt.plot(estimate_results['Gía trị LR'],estimate_results['Tên Biến'])
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Khả Năng Khớp Dữ Liệu Thực Của Mô Hình Logistic',
          fontsize=14,fontweight='bold')
plt.ylabel('Tên Biến Giải Thích Được Thêm Vào', fontsize=11)
plt.xlabel('Chỉ số Thống Kê LR Chi-squared', fontsize=11)
plt.show()


# ### <a href='#Valid_1014'>Biến Động Chỉ Số Pseudo-R-squared</a>
# Chỉ số Pseudo-R-squared cũng là một trong những chỉ số cho biết khả năng phản ánh của Mô Hinh Logistic với dữ liệu thực. Do đó, chúng tôi tiến hành phân tích tích độ nhạy của Mô Hình Logistic qua sự biến động của chỉ số Pseudo-R-Squared với việc thêm/bơt lần lượt từng biến giải thích.

# In[33]:


fig = plt.figure(figsize=(10,5))
plt.plot(estimate_results['pseudo-R-squared'],estimate_results['Tên Biến'])
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Khả Năng Khớp Dữ Liệu Thực Của Mô Hình Logistic',
          fontsize=14,fontweight='bold')
plt.ylabel('Tên Biến Giải Thích Được Thêm/Bớt', fontsize=11)
plt.xlabel('Chỉ số Pseudo-R-squared', fontsize=11)
plt.show()


# ### <a href='#Valid_1015'>Sự phức tạp của Mô Hình</a>
# 
# $$AIC=2*k- 2*Log(\hat{L})$$
# $$BIC=Log(N)*k- 2*Log(\hat{L})$$

# In[34]:


fig = plt.figure(figsize=(10,5))
plt.plot(estimate_results['AIC'],estimate_results['Tên Biến'],
        Linestyle='-.',label='AIC')
plt.plot(estimate_results['BIC'],estimate_results['Tên Biến'],
        Linestyle='-',label='BIC')
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Sự Phức Tạp Của Mô Hình',
          fontsize=14,fontweight='bold')
plt.ylabel('Tên Biến Giải Thích Được Thêm/Bớt', fontsize=11)
plt.xlabel('Chỉ số AIC/BIC', fontsize=11)
plt.legend()
plt.show()


# ###  <a href='#Valid_12'>Độ Nhạy Của Mô Hình Với Số Biến Giải Thích </a> 
# 
# Trong trường hợp này, để phân tích độ Nhạy của Mô Hình Logistic, chúng tôi chọn yếu tố đầu ra của Mô Hình là là kết quả dự báo, và yếu tố đầu vào thay đổi là Số Biến giải thích. Cụ thể chúng tôi sẽ kiểm chứng xem, khi chúng tôi thay đổi số biến đầu vào của Mô Hình Logistic thì khả năng dự báo của nó sẽ là như thế nào. Chỉ tiêu Accuracy sẽ được chọn để lượng hóa Độ Nhạy của Mô Hình Logistic trong tình huống này

# In[38]:


estimator =LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False)
competing_model_score_df = []
score_model = []
numvars = []
training_time=[]
#training_time.append(timer() - start)
print(Red+"Please wait! I am done soon..."+End)
for num in range(len(X_train.columns)):
    start = timer()
    selector_fit=RFE(estimator, num+1, step=1).fit(X_train,Y_train)
    selector_score=selector_fit.score(X_train,Y_train)
    score_model.append(selector_score)
    numvars.append(num+1)
    training_time.append(timer() - start)
compared_results= pd.DataFrame(data={'Số biến trong mô hình':numvars,
                              'Độ nhạy của Mô Hình (Score)':score_model,
                                    'Thời gian (s)':training_time})
print(Bold+'Độ Nhạy Của Mô Hình Logistic Theo Số Biến Giải Thích'+End)
compared_results.sort_values(by=['Độ nhạy của Mô Hình (Score)'],ascending=False)


# In[39]:


sns.set()
fig=plt.figure(figsize=(12,5))
plt.plot(compared_results['Độ nhạy của Mô Hình (Score)'],LineWidth=2)
#plt.autoscale(enable=True,axis='both',tight=True)
plt.title('Độ Nhạy Của Mô Hình Logistic Theo Số Biến Giải Thích',
          fontsize=14,fontweight='bold',color='k')
plt.ylabel('Chỉ Số Accuracy',fontsize=12)
plt.xlabel('Số Biến Giải Thích Trong Mô Hình Logistic',
           fontsize=12,
           fontweight='normal',color='k')


# ###  <a href='#Valid_13'>Độ Nhạy Của Mô Hình Với Số Quan Sát </a> 
# 
# Phần này trả lời cho câu hỏi: Số quan sát sẽ ảnh hưởng như thế nào tới Mô Hình Logistic. Cụ thể, liệu rằng càng nhiều quan sát thì khả năng hoạt động của Mô Hình càng hiệu quả?
# 
# Để thực hiện điều này, chúng ta tiến hành ước lượng mô hình trên các tập dữ liệu có độ lớn khác nhau. Ví dụ, độ lớn của dữ liệu dùng để ước lượng Mô hình Logistic sẽ dần theo tỷ lệ chỉ chiếm từ 10%, 33%,... cho tới toàn bộ 100%. Thêm vào đó, trong mỗi khoảng Dữ liệu đó, chúng ta lại ước lượng Mô hình 100 lần, với tỷ lệ phân chia là 80/20. Cuối cùng, giá trị trung bình phần diện tích nằm dưới đường the Receiver Operating Characteristic Curve (ROC-AUC), sẽ dùng làm thước đo hiệu quả của Mô hình theo thay đổi của kích cỡ dữ liệu đào tạo.
# 
# Kết quả, chúng ta thấy rằng Số Biến quan sát có ảnh hưởng tới hiệu quả hoạt động của Mô Hình Logistic. Cụ thể, nếu chỉ dùng 2000 Quan sát, chúng ta sẽ thấy có hiện tượng Mô Hình Logistic bị nhiều lỗi trong dự báo, và lỗi này giảm đi khi số quan sát tăng lên. Tuy nhiên, số quan sát trên 14000 thì chúng ta không cần thiết phải thu thập thêm dữ liệu nữa. Thay vì đó, để năng cao hoạt động của Mô Hình Logistic thì chúng ta sẽ nghiên cứu ở khía cạnh khác như số biến giải thích hoặc sử dụng các Mô hình khác
# 
# https://www.dataquest.io/blog/learning-curves-machine-learning/
# 
# 
# 

# In[40]:


cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
#cv = KFold(n_splits=10, random_state=7)
estimator=LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False)
X=X_train
y=Y_train
train_sizes=[0.1, 0.33, 0.55, 0.78, 1. ]
print(Red+Bold+"Xin Vui Lòng Đợi, Tôi Đang Tính Toán Mà! "+End)
print(Red+".............. "+End)
start = timer()
train_sizes, train_scores, test_scores = learning_curve(estimator,
                                                            X, y, train_sizes=train_sizes,
                                                            cv=cv, scoring='roc_auc',
                                                            n_jobs=4)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
print(Red+Bold+"Ok! Tôi đã tính toán xong rồi đấy. Hết %.2f Giây bạn nhé "%(timer() - start))


# In[41]:


plt.figure(figsize=(12, 5))
plt.title("Tác Động Của Số Quan Sát Tới Độ Nhạy Học Của Mô Hình",
         fontsize=14,fontweight='bold',color='b')
plt.plot(train_sizes, train_scores_mean, marker='o', color="blue",
             label="Đường Cong Học (Learning Curve) tính trên dữ liệu đào tạo", linestyle='--')
plt.plot(train_sizes, test_scores_mean, marker='v', color="green",
             label="Đường Cong Học (Learning Curve) tính trên dữ liệu kiểm tra")
plt.autoscale(enable=True, axis='both',tight=True)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.ylabel('Phần diện tích dưới đường ROC-AUC',fontsize=12)
plt.xlabel('Số Quan Sát Sử Dụng',
           fontsize=12,
           fontweight='normal',color='k')
plt.legend(loc="best")
   


# ### <a href='#Valid_133'>Deviance Residual  </a> 
# 
# Trong phần phân tích độ nhạy này, chúng tôi kiểm tra yếu tố đầu ra là Deviance Residual của Mô Hình Logistic nếu giả định yếu tố đầu vào là Phần dư thay đổi từ Phân Phổi Thường Chuẩn và Phân Phối Logistic Chuẩn.

# In[1180]:


fig=plt.figure(figsize=(12,5))
fig.add_subplot(1,2,1)
sns.distplot(GLMestimate_results.at[22,'Kết Qủa Ước Lượng'].resid_deviance,
             bins=150, hist=True,kde=True)#, fit=stats.gamma);
plt.title('Histogram \n of Deviance Residual',fontweight='bold')
plt.xlabel('Deviance Residual')
plt.ylabel('Densities')
plt.autoscale(enable=True, axis='both',tight=True)
fig.add_subplot(1,2,2)
stats.probplot(GLMestimate_results.at[22,'Kết Qủa Ước Lượng'].resid_deviance,
               dist="norm", plot=plt)
plt.autoscale(enable=True, axis='both',tight=True)
plt.title("Normal Q-Q plot \n of Deviance Residual",fontweight='bold')
plt.show()


# ### <a href='#Valid_134'>Working Residuals </a> 
# 
# https://www.casact.org/pubs/monographs/papers/05-Goldburd-Khare-Tevet.pdf
# 
# Working residuals are quantities that are used by the IRLS algorithm during the fitting
# process. Careful analysis of the working residuals is an additional tool that can be
# used to assess the quality of model fit.

# In[1184]:


GLMestimate_results.at[i,'Kết Qủa Ước Lượng'].resid_working.head()


# ### <a href='#Valid_136'>Log Loss </a> 
# 
# This is the loss function used in (multinomial) logistic regression and extensions of it such as neural networks, defined as the negative log-likelihood of the true labels given a probabilistic classifier’s predictions. The log loss is only defined for two or more labels. For a single sample with true label yt in {0,1} and estimated probability yp that yt = 1, the log loss is
# 
# $$-log P(yt|yp) = -(yt log(yp) + (1 - yt) log(1 - yp))$$

# In[1359]:


var_nam=[]
Log_loss=[]
kfold = model_selection.KFold(n_splits=20, random_state=7)
estimator_logit=LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False)
print(Red+Bold+"Xin Vui Lòng Đợi, Tôi Đang Tính Toán Mà! "+End)
print(Red+".............. "+End)
start = timer()
for i, colnam in enumerate(X_train.columns):
    cv_LogLossResults = model_selection.cross_val_score(estimator_logit, X_train[X_train.columns[0:i+1]],
                                                        Y_train,cv=kfold, scoring='neg_log_loss')                                    
    var_nam.append(colnam)
    Log_loss.append(cv_LogLossResults)
print(Red+Bold+"Ok! Tôi đã tính toán xong rồi đấy. Hết %.2f Giây bạn nhé. Bạn xem Đồ Thị Đi này "%(timer() - start))    
    
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
plt.boxplot(Log_loss,vert=False, showmeans=True)  
#ax.set_yticklabels(names)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Biến Động Gía Trị Log Loss Của Mô Hình Logistic Với Số Biến Giải Thích',
          fontsize=14,fontweight='bold')
plt.ylabel('Số Biến Giải Thích', fontsize=11)
plt.xlabel('Phân phối Gía Trị Log Loss', fontsize=11)
plt.show()


# ### <a href='#Valid_135'>Cook’s Distance </a> 
# Cook’s Distance is a measure of an observation or instances’ influence on a linear regression. Instances with a large influence may be outliers and datasets that have a large number of highly influential points might not be good predictors to fit linear models.

# In[1203]:


CookDisVisual= CooksDistance()
print(Red+Bold+"Bạn Cứ Bình Tĩnh. Tôi Đang Tính Cook's Distance Cho Bạn Mà! Đừng Tắt Máy Tính nhé! "+End)
print(Red+".............. "+End)
start = timer()
CookDisVisual.fit(X_train, Y_train)
print(Bold+Blue+"Đây! Tôi đã tính toán xong và vẽ đồ thị về Cook's Distance ở dưới cho Bạn rồi đấy. Hết %.2f Phút bạn nhé.  "%((timer() - start)/60)+End)
CookDisVisual.show()


# ### <a href='#Valid_1399'>Thống Kê Kolmogorov–Smirnov (KS) </a> 
# 
# Thống Kê KS được sử dụng phổ biến trong industry
# 
# https://www.accenture.com/gb-en/~/media/accenture/conversion%20assets/dotcom/documents/global/pdf/dualpub_7/accenture-credit-risk-model-monitoring.pdf
# 
# https://www.listendata.com/2019/07/KS-Statistics-Python.html

# In[929]:


logreg=LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False)
logreg_fitted=logreg.fit(X_train, Y_train)
get_prob_train=pd.DataFrame(logreg_fitted.predict_proba(X_train))

ks_train=pd.DataFrame({'prob':get_prob_train[1],
                      'target':Y_train},)

ks_train['target0'] = 1 - ks_train['target']
ks_train['bucket'] = pd.qcut(ks_train['prob'], 10)
grouped = ks_train.groupby('bucket', as_index = False)
kstable_train = pd.DataFrame()
kstable_train['min_prob'] = grouped.min()['prob']
kstable_train['max_prob'] = grouped.max()['prob']
kstable_train['events']   = grouped.sum()['target']
kstable_train['nonevents'] = grouped.sum()['target0']
kstable_train = kstable_train.sort_values(by="min_prob", ascending=False).reset_index(drop = True)
kstable_train['event_rate'] = (kstable_train.events / ks_train['target'].sum()).apply('{0:.2%}'.format)
kstable_train['nonevent_rate'] = (kstable_train.nonevents / ks_train['target0'].sum()).apply('{0:.2%}'.format)
kstable_train['cum_eventrate']=(kstable_train.events / ks_train['target'].sum()).cumsum()
kstable_train['cum_noneventrate']=(kstable_train.nonevents / ks_train['target0'].sum()).cumsum()
kstable_train['KS'] = np.round(kstable_train['cum_eventrate']-kstable_train['cum_noneventrate'], 3) * 100
kstable_train

kstable_train['cum_eventrate']= kstable_train['cum_eventrate'].apply('{0:.2%}'.format)
kstable_train['cum_noneventrate']= kstable_train['cum_noneventrate'].apply('{0:.2%}'.format)
kstable_train.index = range(1,11)
kstable_train.index.rename('Decile', inplace=True)
pd.set_option('display.max_columns', 9)

print(Blue+Bold + "Gía Trị Thống Kê Kolmogorov–Smirnov (In-sample) Là %.2f "%max(kstable_train['KS']) +"%"+      " Tại điểm Thứ %d Của Dữ Liệu"%      (kstable_train.index[kstable_train['KS']==max(kstable_train['KS'])][0]))
kstable_train


# ### <a href='#Valid_134'>Ma Trận Confusion  </a> 
# 
# Chúng tôi quan sát thấy rằng, Ma Trận Confusion là cách tiếp cận phổ biến trong Industry cũng như trong phát triển các Chương Trình Máy Học/AI. Vì vậy, trong nội dung này chúng tôi cũng sẽ phân tích độ nhạy của Mô Hình Logistic dựa trên hướng tiếp cận này

# In[665]:


Y_Fitted = logreg_fitted.predict(X_train)
print(Blue+'Khả Năng Dự Báo Của Mô Hình Logistic (In-sample Forecast): {:.2f}'.      format(logreg.score(X_train, Y_train))+End)
confus_matrix = confusion_matrix(Y_train, Y_Fitted)


# In[960]:


group_names = ['Dự Báo Đúng Không Xảy Ra Vỡ Nợ \n (True Negative)',
               'Dự Báo Sai Có Xảy Ra Vỡ Nợ \n (False Positive)\n Type I Error',
               'Dự Báo Sai Không Xảy Vỡ Nợ \n (False Negative)\n Type II Error',
               'Dự Báo Đúng Có Xảy Ra Vỡ Nợ \n (True Positive)']
group_counts = ["{0:0.0f}".format(value) for value in
                confus_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
                     confus_matrix.flatten()/np.sum(confus_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
accuracy  = np.trace(confus_matrix) / float(np.sum(confus_matrix))
precision = confus_matrix[1,1] / sum(confus_matrix[:,1])
recall    = confus_matrix[1,1] / sum(confus_matrix[1,:])
f1_score  = 2*precision*recall / (precision + recall)
stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy,precision,recall,f1_score)
plt.figure(figsize=(12, 7))
plt.title("Ma Trận Confusion \n (In-sample Forecast)",fontsize=14,
          fontweight='bold',color='tab:orange')
sns.heatmap(confus_matrix,center=True, annot=labels, fmt='', cmap='Oranges')
plt.ylabel('Gía Trị Thực Tế',fontsize=12,
          fontweight='bold',color='tab:orange')
plt.xlabel('Gía Trị Dự Báo Của Mô Hình Logistic \n (In-sample Forecast)',fontsize=12,
          fontweight='bold',color='tab:orange')
#plt.xlabel(stats_text)
plt.show()


# ### <a href='#Valid_135'>Chỉ Tiêu AUROC </a> 

# In[556]:


FPR=[]
TPR=[]
roc_auc_train=[]
FPR_valid=[]
TPR_valid=[]
roc_auc_valid=[]
Model_nume=[]
var_name=[]
print(Red+"Xin vui lòng đợi tôi tý nhé....."+End)
for i, colnam in enumerate(X_train.columns):
    mylogreg=LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False)
    mylogreg.fit(X_train[X_train.columns[0:i+1]], Y_train)
    logit_roc_auc = roc_auc_score(Y_train, mylogreg.predict(X_train[X_train.columns[0:i+1]]))
    fpr, tpr, thresholds = roc_curve(Y_train, 
                                     mylogreg.predict_proba(X_train[X_train.columns[0:i+1]])[:,1])
    roc_auc_train.append(auc(fpr,tpr))
    Model_nume.append(i+1)
    var_name.append(colnam)
    FPR.append(fpr)
    TPR.append(tpr)
    
    fpr_valid, tpr_valid, thresholds_valid = roc_curve(Y_valid, 
                                     mylogreg.predict_proba(X_valid[X_valid.columns[0:i+1]])[:,1])

    

    logit_roc_auc_valid = roc_auc_score(Y_valid, 
                                        mylogreg.predict(X_valid[X_valid.columns[0:i+1]]))
    fpr_valid, tpr_valid, thresholds_valid = roc_curve(Y_valid,
                                                       mylogreg.predict_proba(X_valid[X_valid.columns[0:i+1]])[:,1])#)
    

    roc_auc_valid.append(auc(fpr_valid,tpr_valid))
    FPR_valid.append(fpr_valid)
    TPR_valid.append(tpr_valid)
    
print(Red+"Cảm ơn bạn đã chờ. Tôi làm xong rồi ấy. In kết quả ra đi"+End)
roc_results= pd.DataFrame(data={'Mô Hình':Model_nume,
                                     'Tên Biến':var_name,
                                    'Gía trị TPR':TPR,
                                     'Gía trị FPR':FPR,
                               'Diện tích':roc_auc_train,
                               'Gía trị TPR_valid':TPR_valid,
                               'Gía trị FPR_valid':FPR_valid,
                               'Diện tích valid':roc_auc_valid,},)


# In[1353]:


plt.figure(figsize=(12, 5))
plt.plot(roc_results.at[0,'Gía trị FPR'],
         roc_results.at[0,'Gía trị TPR'],
         label='Mô Hình Logistic %d biến (Diện tích =%.2f)'%(roc_results.at[0,'Mô Hình'],
                                                        roc_results.at[0,'Diện tích']),
        linestyle=':')
plt.plot(roc_results.at[4,'Gía trị FPR'],
         roc_results.at[4,'Gía trị TPR'],
         label='Mô Hình Logistic %d biến (Diện tích =%.2f)'%(roc_results.at[4,'Mô Hình'],
                                                        roc_results.at[4,'Diện tích']),
        linestyle='-.')


plt.plot(roc_results.at[22,'Gía trị FPR'],
         roc_results.at[22,'Gía trị TPR'],
         label='Mô Hình Logistic %d biến (Diện tích =%.2f)'%(roc_results.at[22,'Mô Hình'],
                                                        roc_results.at[22,'Diện tích']),
        linestyle='--')
plt.plot([0, 1], [0, 1], color='navy', linestyle='-')
plt.autoscale(enable=True, axis='both',tight=True)
plt.suptitle('Biến động AUC-ROC Của Mô Hình Logistic Theo Số Biến Giải Thích',
          fontsize=15,fontweight='bold',color='b')
plt.title('(In-Sample Sensitivity Analysis)',
          fontsize=15,fontweight='bold',color='b')
plt.ylabel('Chỉ Số Sensitivity', fontsize=12,color='b',fontweight='bold')
plt.xlabel('Chỉ Số Specificity',fontsize=12,color='b',fontweight='bold')
plt.legend(loc="lower right")

plt.show()


# ### <a href='#Valid_1350'>Bootstrap Analysis AUROC </a> 

# In[1698]:


n_bootstraps = 1000
rng_seed = 42  # control reproducibility
bootstrapped_scores_train = []
rng = np.random.RandomState(rng_seed)
for i in range(n_bootstraps):
    # bootstrap by sampling with replacement on the prediction indices
    indices = rng.randint(0, len(Y_Fitted), len(Y_Fitted))
    if len(np.unique(Y_train[indices])) < 2:
        # We need at least one positive and one negative sample for ROC AUC
        # to be defined: reject the sample
        continue

    score_roauc_train = roc_auc_score(Y_train[indices], Y_Fitted[indices])
    bootstrapped_scores_train.append(score_roauc_train)
    #print("Bootstrap #{} ROC area: {:0.3f}".format(i + 1, score))

plt.figure(figsize=(13, 5))
sns.distplot(bootstrapped_scores_train, bins=50, kde=True,hist=True)
plt.suptitle('Histogram of %d Boostrap for ROAUC scores \n (In-sample)'%len(bootstrapped_scores_train),
         fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tần Xuất', fontweight='bold',
           color='b',fontsize=12)
plt.xlabel('Chỉ Số ROAUC',fontweight='bold',fontsize=12,color='b')
plt.show()


# ### <a href='#Valid_1351'>Khoảng Tin Cậy Cho AUROC </a> 

# In[1819]:


Num_bootstrap=[]
lopbootstrapped_scores_train=[]
noboot=[10,20,50,100,500,800,1000]
for i,n_boostrap in enumerate(noboot):
    #print(i,n_boostrap)
    Num_bootstrap.append(n_boostrap)
    lopbootstrapped_scores_train.append([])
    rng_seed = 42  # control reproducibility
    loprng_train = np.random.RandomState(rng_seed)
    for i_bot in range(n_boostrap):
        #print(i_bot)
        indices_trainlop = loprng_train.randint(0, len(Y_Fitted), len(Y_Fitted))
        if len(np.unique(Y_train[indices_train])) < 2:
            continue
        lopscore_roauc_train = roc_auc_score(Y_train[indices_trainlop ], Y_Fitted[indices_trainlop ])
        lopbootstrapped_scores_train[i].append(lopscore_roauc_train)
#lopbootstrapped_scores_train      

confidence_lower_lop_train=[]
confidence_upper_lop_train=[]
for i in range(len(lopbootstrapped_scores_train)):
    #rint(i)
    sorted_scores_lop_train = np.array(lopbootstrapped_scores_train[i])
    sorted_scores_lop_train.sort()
    confidence_lower_lop_train.append(round(sorted_scores_lop_train[int(0.05 * len(sorted_scores_lop_train))],4))
    confidence_upper_lop_train.append(round(sorted_scores_lop_train[int(0.95 * len(sorted_scores_lop_train))],4))


print(Bold+'Khoảng Tin Cậy 95(%) Của AUROC Qua Các Lần Bootstrap Khác Nhau (In-Sample)'+End)
print(pd.DataFrame({'Số Bootstrap':Num_bootstrap,
             'Lower Bound':confidence_lower_lop_train,
             'Upper Bound':confidence_upper_lop_train}))


# ### <a href='#Valid_136'>Hệ Số Gini (Accuracy Ratio AR) </a> 

# In[772]:


Gini_train=[]
for i in range(0,len(roc_results)):
    Gini_train.append(2*roc_results.at[i,'Diện tích']-1)
plt.figure(figsize=(12, 5))
plt.suptitle('Biến động Hệ Số Gini Của Mô Hình Logistic Theo Số Biến Giải Thích \n In-Sample',
          fontsize=15,fontweight='bold',color='b')
plt.plot(Gini_train, color='navy', linestyle='-', label='Hệ Số Gini')
plt.xlabel('Số Biến Giải Thích Trong Mô Hình', fontweight='bold',
           color='b',fontsize=12)
plt.ylabel('Hệ Số Gini',fontweight='bold',fontsize=12,color='b')
plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.show()


# ### <a href='#Valid_1367'>Bootstrap for Gini (Accuracy Ratio AR) </a> 

# In[1683]:


bootstrapped_GINI_train=[(2*p-1) for p in bootstrapped_scores_train]
plt.figure(figsize=(13, 5))
sns.distplot(bootstrapped_GINI_train, bins=50, kde=True,hist=True)
plt.suptitle('Histogram of %d Boostrap for GINI (Accuracy Ratio AP) \n (In-sample)'%len(bootstrapped_scores_train),
         fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tần Xuất', fontweight='bold',
           color='b',fontsize=12)
plt.xlabel('Chỉ Số GINI (Accuracy Ratio AP) ',fontweight='bold',fontsize=12,color='b')
plt.show()


# ### <a href='#in_sam18'>CAP – Cumulative Accuracy Profile </a>   

# In[962]:


total_train = len(Y_train) 
 # Đếm Số Vỡ Nợ Trong Dữ Liệu     
one_count_train = np.sum(Y_train) 
# Đếm Số Không Vỡ Nợ Trong Dữ Liệu
zero_count_train = total_train - one_count 
  
lm_train = [y for _, y in sorted(zip(Y_Fitted, Y_train), reverse = True)] 
x_axis_train = np.arange(0, total_train + 1) 
y_axis_train = np.append([0], np.cumsum(lm_train)) 


plt.figure(figsize = (10, 6))  
plt.plot([0, total_train], [0, one_count_train], c = 'b',  
         linestyle = '-', label = 'Mô Hình Ngẫu Nhiên') 
plt.plot(x_axis_train, y_axis_train, c = 'b', label = 'Mô Hình Logistic',
         linestyle = ':',linewidth = 6) 
plt.plot([0, one_count_train, total_train], 
         [0, one_count_train, one_count_train], linestyle = '-.',
         c = 'grey', linewidth = 2, label = 'Mô Hình Hoàn Hảo') 
plt.suptitle('Phân Tích CAP Của Mô Hình Logistic \n In-Sample Forecast',
          fontsize=15,fontweight='bold',color='b')
plt.xlabel('Số Người Nợ Ngân Hàng', fontweight='bold',
            color='b',fontsize=12)
plt.ylabel('Số Người Bị Vỡ Nợ Ngân Hàng',fontweight='bold',fontsize=12,color='b')
plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.show()


# ### <a href='#in_sample70'>In-Sample Discriminatory Power Của Mô Hình Logistic </a> 

# In[740]:


target_names = ['Không Xảy Ra Vỡ Nợ', 'Xảy Ra Vỡ Nợ']
print(Bold+'Báo Cáo Khả Năng Phân Loại giữa Xảy Ra Và Không Xảy Ra Vỡ Nợ Của Mô Hình Logistic \n In-Sample'+End)
print(classification_report(Y_train, Y_Fitted, target_names=target_names))


# ### <a href='#in_sample71'>Plotting In-Sample Discriminatory Power Của Mô Hình Logistic </a> 

# In[1202]:


visualizer = DiscriminationThreshold(LogisticRegression(solver='liblinear',
                                                        penalty='l1',fit_intercept=False))

visualizer.fit(X_train, Y_train)        
visualizer.show()           


# ### <a href='#in_sample09'>Lorenz Curve</a> 
# https://www.kaggle.com/batzner/gini-coefficient-an-intuitive-explanation

# In[1284]:


Lor_data = zip(Y_train, Y_Fitted)
sorted_Lor_data = sorted(Lor_data, key=lambda d: d[1])
sorted_Lor_actual = [d[0] for d in sorted_Lor_data]


lorenz = np.cumsum(sorted_Lor_actual) / np.sum(sorted_Lor_actual)
lorenz = np.insert(lorenz, 0, 0) 
lorenz[0], lorenz[-1]

plt.figure(figsize = (10, 6))  
plt.plot(np.arange(lorenz.size)/(lorenz.size-1), lorenz, linestyle = '-.',
            linewidth = 2,color='darkgreen',label='Lorenz Curve ')
plt.plot(np.arange(lorenz.size)/(lorenz.size-1),
         np.arange(lorenz.size)/(lorenz.size-1), 
         linewidth = 1,color='r',label='Line of Equality')
plt.fill_between(np.arange(lorenz.size)/(lorenz.size-1),
                 np.arange(lorenz.size)/(lorenz.size-1), lorenz,
                 color='C1', alpha=0.7,
                 label='Gini Index')

plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.suptitle('Đường Cong Lorenz\n In-Sample Validation',
          fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tỷ Lệ Gía Trị Thực Lũy Tiến \n Cumulative Share of Actual Values',
           fontweight='bold',fontsize=12,color='b')
plt.xlabel('Tỷ Lệ Dự Báo Lũy Tiến \n Cumulative Share of Predictions', fontweight='bold',
            color='b',fontsize=12)
plt.show()


# ### <a href='#in_sample91'>Điểm Brier và Calibration Plots</a> 
# 
# The position of the points or the curve relative to the diagonal can help to interpret the probabilities; for example:
# 
# - Below the diagonal: The model has over-forecast; the probabilities are too large.
# - Above the diagonal: The model has under-forecast; the probabilities are too small.
# 
# https://machinelearningmastery.com/how-to-calculate-nonparametric-rank-correlation-in-python/

# In[1446]:


Y_pred_train = logreg_fitted.predict(X_train)
Default_Pred_prob_train = logreg_fitted.predict_proba(X_train)[:, 1]
NonDef_Pred_prob_train = logreg_fitted.predict_proba(X_train)[:, 0]

Default_brier_score_train=brier_score_loss(Y_train, Default_Pred_prob_train, 
                                           pos_label=Y_train.max())
NonDef_brier_score_train=brier_score_loss(Y_train, NonDef_Pred_prob_train , 
                                           pos_label=Y_train.max())

fraction_of_default_train, Default_mean_predicted_value_train =             calibration_curve(Y_train, Default_Pred_prob_train, n_bins=50)
fraction_of_nondefault_train, NonDef_mean_predicted_value_train =             calibration_curve(Y_train, NonDef_Pred_prob_train, n_bins=50)

fig=plt.figure(figsize=(12,5))
plt.suptitle('Calibration plots  (reliability curve)')
fig.add_subplot(1,2,1)
plt.plot(Default_mean_predicted_value_train, fraction_of_default_train, "s-",
                 label="The Brier Score of Logistic Model for Default (%1.3f)" % (Default_brier_score_train))
plt.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
plt.autoscale(enable=True,axis='x',tight=True)
plt.ylabel("Tỷ Lệ Vỡ Nợ")

plt.xlabel("Gía Trị Xác Xuất Dự Báo Trung Bình Cho Trường Hợp Vỡ Nợ")
plt.legend(loc="upper left")

fig.add_subplot(1,2,2)
plt.plot(NonDef_mean_predicted_value_train, fraction_of_nondefault_train, "s-",
                 label="The Brier Score of Logistic Model for NonDefault (%1.3f)" % (NonDef_brier_score_train))
plt.plot([0, 1], [1, 0], "k:", label="Perfectly calibrated")
plt.autoscale(enable=True,axis='x',tight=True)
plt.ylabel("Tỷ Lệ Không Vỡ Nợ")

plt.xlabel("Gía Trị Dự Báo Trung Bình")
plt.legend(loc="upper left")


#fig.add_subplot(1,2,2)
#plt.hist(Default_Pred_prob_train, range=(0, 1), bins=10, label=name,
#                histtype="step", lw=2)
#plt.ylabel("Tần Xuất")
#plt.xlabel("Gía Trị Dự Báo Trung Bình")
plt.show()


# ### <a href='#insmap1791'>The Information Entropy </a>  
# 
# Theo định nghĩa của Uỷ Ban Basel (Basel II), The Information Entropy $H(p)$ của một sự kiên có xác xuất xảy ra là $p$ được tính như sau
# 
# $$H(p) = -\Big[p*log(p) +(1-p)*log(1-p)\Big]$$
# 
# Tuy nhiên chúng tôi không áp dụng công thưc trên của Basel, với ly do, ý nghĩa của công thức trên là giá trị kỳ vọng của sự kienj vỡ nợ. Cụ thể, chúng tôi tính Entropy cho Vỡ Nợ như sau
# 
# $$H(p) = -\Big[p*log(p)\Big]$$
# 
# Đây là cách tiếp cận phổ biến khi chúng tôi nghiên cứu các tài liệu khác ngoài Khuyến nghị của Basel II.
# 
# The intuition behind quantifying information is the idea of measuring how much surprise there is in an event. Those events that are rare (low probability) are more surprising and therefore have more information those events that are common (high probability).
# 
# - Low Probability Event: High Information (surprising).
# - High Probability Event: Low Information (unsurprising).

# In[1520]:


info_entro_defTrain = [-(p*log2(p)+(1-p)*log2(1-p)) for p in Default_Pred_prob_train]
fig=plt.figure(figsize=(12,5))
plt.scatter(Default_Pred_prob_train, info_entro_defTrain, marker='.')
plt.title('Xác Xuất Dự Báo Từ Mô Hình Logistic Và Chỉ Số Information Entropy Xảy Ra Vỡ Nợ\n (In-Sample)',
         fontsize=15,fontweight='bold',color='b')
plt.xlabel('Xác Xuất Dự Báo Từ Mô Hình Logistic',
          fontsize=12,fontweight='bold',color='b')
plt.ylabel('Chỉ Số Information Entropy',
          fontsize=12,fontweight='bold',color='b')
plt.show()


# ### <a href='#insmap1792'>Kullback-Leibler Distance </a>  
# 
# Theo định nghĩa Basel II:
#     
# $$Kullback-Leibler Distance = H(p) − HS$$

# In[1519]:


conEn_train=drv.entropy_conditional(Y_Fitted.tolist(),Y_train.tolist())


# In[ ]:





# In[1516]:


Y_train[:3].tolist()


# In[1518]:





# In[1490]:


NonDef_Pred_prob_train


# In[1492]:


#drv.entropy_conditional(Default_Pred_prob_train,NonDef_Pred_prob_train)


# ### <a href='#insmap179'>Precision-Recall Curve </a>  

# In[1351]:


average_precision_train = average_precision_score(Y_train, Y_Fitted)  
disp = plot_precision_recall_curve(logreg_fitted, X_train, Y_train)
disp.ax_.set_title('2-class Precision-Recall curve\n In-sample Validation \nAP={0:0.2f}'.format(average_precision_valid))
plt.show()


# In[1824]:


X1 = np.random.multivariate_normal([-1, 0], [[1, 0], [0, 1]], 100)


# ### <a href='#in_sam45'>In-Sample Prediction Error </a>   

# In[1360]:


classes = ['Không Có Rủi Ro Vỡ Nợ', 'Rủi Ro Vỡ Nợ']
Logit_PredErVisual= ClassPredictionError(LogisticRegression(solver='liblinear',
                                                        penalty='l1',fit_intercept=False),
                                        classes=classes)
Logit_PredErVisual.fit(X_train, Y_train)  
Logit_PredErVisual.score(X_train, Y_train)  
plt.figure(figsize = (10, 6)) 
Logit_PredErVisual.show()               


# ### <a href='#in_sample79'>Đường Cong Kiểm Định (Validation Curve)</a> 

# In[1232]:


cv = StratifiedKFold(12)
param_range = np.linspace(0.1,2,10)
viz = ValidationCurve(
    LogisticRegression(solver='liblinear',penalty='l1',fit_intercept=False),
    param_name='C', param_range=param_range,
    logx=True, cv=cv, scoring="accuracy", n_jobs=8,
)
viz.fit(X_train,Y_train)
viz.show()


# ### <a href='#in_sample793'>Xác Xuất Vỡ Nợ (PD) Và Tỷ Lệ Duyệt Khoản Vay</a> 

# In[1648]:


threshold_accepted_train = np.quantile(Default_Pred_prob_train, 0.85)
fig=plt.figure(figsize=(12,5))
plt.suptitle('Gía Trị Xác Xuất (PD) Ứớc Lượng Từ Mô Hình Logistic và Ngưỡng Duyệt Khoản Vay \n (In-Sample Forecast)')
sns.distplot(Default_Pred_prob_train,hist=True,rug=False,
             kde_kws={'linestyle':'--'},label='PD Ước Lượng')
plt.axvline(threshold_accepted_train,lw='3',color='r')#,
            #label='Gía Trị Ngưỡng Một Khoản Vay Được Duyệt')
plt.annotate('\n Gía Trị Ngưỡng (%.2f) \n Một Khoản Vay \n Được Duyệt'%threshold_accepted_train, 
             xy=(0.66, 4.2), xytext=(0.7, 4),
           arrowprops=dict(facecolor='r', shrink=0.01))

plt.ylabel("Tần Xuất")

plt.xlabel("The In-Sample Probability of Default (PD)")
plt.legend(loc="lower left")
plt.show()


# $$\Large \color{blue}{\textbf{Phần V: Giam Sát Hoạt Động Của Mô Hình}}$$
#  
#  $$\Large \color{blue}{\textbf{Model Monitoring}}$$
#     
#  $$\Large \color{blue}{\textbf{Out-Of-Sample Sentivitity Analysis and Validation}}$$
# 
# ## <a href='#Valid_2'>Out-of-sample (Model Monitoring) </a> 
# 
# Phần này chúng ta sẽ tiến hành Giam sát hoạt động của Mô Hình, cụ thể chúng ta sẽ theo hướng tiếp cận của Industry như của Ủy Ban Basel, Ngân Hàng Trung ương Đức (Bundesbank), Của Công Ty Xếp Hạng Tín Nhiệm Moody hay Finity của Úc, etc..Đặc biệt, chúng tôi tập trung theo những khuyến nghị của Uỷ Ban Basel.Do đó, các chỉ tiêu sau được chúng tôi sử dụng như
# 
# 1. Hệ Số Gini.
# 
# 2. Chỉ số AUC-ROC
# 
# 3. Chỉ tiêu K-P. 
# 
# 4. Ma Trận Confustion.
# 
# 5. Khả năng Phân Loại (Classification Report)
# 
# 3. Lỗi loại I, Lỗi loại II.
# 
# Tham khảo kỹ hơn về giám sát Mô Hình tại các trang sau
# 
# https://www.bis.org/publ/bcbs_wp14.pdf
# 
# https://www.bis.org/ifc/events/ws_micro_macro/nehrebecka_paper.pdf
# 
# 
# https://www.bundesbank.de/resource/blob/704150/b9fa10a16dfff3c98842581253f6d141/mL/2003-10-01-dkp-01-data.pdf
# 
# 
# https://www.crowe.com/insights/credit-risk-model-validation
# 
# https://www.moodysanalytics.com/-/media/products/Model-Monitoring.pdf
# 
# https://www.finity.com.au/wp-content/uploads/2014/05/07.-Model-monitoring.pdf
# 
# https://www.accenture.com/gb-en/~/media/accenture/conversion%20assets/dotcom/documents/global/pdf/dualpub_7/accenture-credit-risk-model-monitoring.pdf

# ### <a href='#out_of90'>Out-Of-Sample Predictor Error </a>    

# In[1215]:


classes = ['Không Có Rủi Ro Vỡ Nợ', 'Rủi Ro Vỡ Nợ']
Logit_PredErVisual= ClassPredictionError(LogisticRegression(solver='liblinear',
                                                        penalty='l1',fit_intercept=False),
                                        classes=classes)
Logit_PredErVisual.fit(X_train, Y_train) 
Logit_PredErVisual.score(X_valid, Y_valid)  
plt.figure(figsize = (10, 6)) 
Logit_PredErVisual.show()     


# ### <a href='#out_of9'>Out-Of-Sample Confusion Matrix </a>    

# In[724]:


Y_Forecast= logreg_fitted.predict(X_valid)
print(Blue+'Khả Năng Dự Báo Của Mô Hình Logistic (Out-Of-sample Forecast): {:.2f}'.      format(logreg.score(X_valid, Y_valid))+End)
confus_matrix_valid = confusion_matrix(Y_valid, Y_Forecast)


# In[938]:


group_names = ['Dự Báo Đúng Không Xảy Ra Vỡ Nợ \n (True Negative)',
               'Dự Báo Sai Có Xảy Ra Vỡ Nợ \n (False Positive)\n Type I Error',
               'Dự Báo Sai Không Xảy Vỡ Nợ \n (False Negative)\n Type II Error',
               'Dự Báo Đúng Có Xảy Ra Vỡ Nợ \n (True Positive)']
group_counts = ["{0:0.0f}".format(value) for value in
                confus_matrix.flatten()]
group_percentages = ["{0:.2%}".format(value) for value in
                     confus_matrix.flatten()/np.sum(confus_matrix)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in
          zip(group_names,group_counts,group_percentages)]
labels = np.asarray(labels).reshape(2,2)
accuracy_valid  = np.trace(confus_matrix_valid) / float(np.sum(confus_matrix_valid))
precision_valid = confus_matrix_valid[1,1] / sum(confus_matrix_valid[:,1])
recall_valid    = confus_matrix_valid[1,1] / sum(confus_matrix_valid[1,:])
f1_score_valid  = 2*precision_valid*recall_valid / (precision_valid + recall_valid)
stats_text = "\n\nAccuracy={:0.3f}\nPrecision={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
                accuracy_valid,precision_valid,recall_valid,f1_score_valid)
plt.figure(figsize=(15, 7))
plt.title("Ma Trận Confusion \n (Out-Of-sample Forecast)",fontsize=14,
          fontweight='bold',color='tab:orange')
sns.heatmap(confus_matrix_valid,center=True, annot=labels, fmt='', cmap='Oranges')
plt.ylabel('Gía Trị Thực Tế',fontsize=12,
          fontweight='bold',color='tab:orange')
plt.xlabel('Gía Trị Dự Báo Của Mô Hình Logistic \n (Out-Of-sample Forecast)',fontsize=12,
          fontweight='bold',color='tab:orange')
#plt.xlabel(stats_text)
plt.show()


# ### <a href='#out_of1'>Out-Of-Sample AU-ROC </a>    

# In[758]:


plt.figure(figsize=(12, 5))
plt.plot(roc_results.at[0,'Gía trị FPR_valid'],
         roc_results.at[0,'Gía trị TPR_valid'],
         label='Mô Hình Logistic %d biến (AUC-ROC =%.2f)'%(roc_results.at[0,'Mô Hình'],
                                                        roc_results.at[0,'Diện tích valid']),
        linestyle=':')
plt.plot(roc_results.at[4,'Gía trị FPR_valid'],
         roc_results.at[4,'Gía trị TPR_valid'],
         label='Mô Hình Logistic %d biến (AUC-ROC =%.2f)'%(roc_results.at[4,'Mô Hình'],
                                                        roc_results.at[4,'Diện tích valid']),
        linestyle='-.')


plt.plot(roc_results.at[22,'Gía trị FPR_valid'],
         roc_results.at[22,'Gía trị TPR_valid'],
         label='Mô Hình Logistic %d biến (AUC-ROC =%.2f)'%(roc_results.at[22,'Mô Hình'],
                                                        roc_results.at[22,'Diện tích valid']),
        linestyle='--')

plt.suptitle('Biến động Chỉ Số AUC-ROC Của Mô Hình Logistic Theo Số Biến Giải Thích',
          fontsize=15,fontweight='bold')
plt.title('Out-Of-Sample',
          fontsize=15,fontweight='bold')
plt.plot([0, 1], [0, 1], color='navy', linestyle='-')
plt.xlabel('Chỉ Số Specificity', fontweight='bold',fontsize=12)
plt.ylabel('Chỉ Số Sensitivity',fontweight='bold',fontsize=12)
plt.legend(loc="lower right")
plt.show()


# ### <a href='#out_of191'>Bootstrap AU-ROC </a>    

# In[1710]:


y_valid=Y_valid
y_valid=np.asarray(y_valid)

n_bootstraps = 1000
rng_seed = 12  # control reproducibility
bootstrapped_scores_valid = []
rng_valid = np.random.RandomState(rng_seed)
for i in range(n_bootstraps):
    indices_valid = rng_valid.randint(0, len(Y_Forecast), len(Y_Forecast))
    #print(indices_valid)

    if len(np.unique(y_valid[indices_valid])) < 2:
        continue
    score_roauc_valid = roc_auc_score(y_valid[indices_valid], Y_Forecast[indices_valid])
    bootstrapped_scores_valid.append(score_roauc_valid)

plt.figure(figsize=(13, 5))
sns.distplot(bootstrapped_scores_valid, bins=50, kde=True,hist=True)
plt.suptitle('Distribution of %d Boostrap for ROAUC scores \n (Out-Of-Sample)'%len(bootstrapped_scores_valid),
         fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tần Xuất', fontweight='bold',
           color='b',fontsize=12)
plt.xlabel('Chỉ Số ROAUC',fontweight='bold',fontsize=12,color='b')
plt.show()


# ### <a href='#outofSam_1351'>Khoảng Tin Cậy Cho AUROC </a> 

# In[1823]:


Num_bootstrap_valid=[]
lopbootstrapped_scores_valid=[]
noboot=[10,20,50,100,500,800,1000]
for i,n_boostrap in enumerate(noboot):
    #print(i,n_boostrap)
    Num_bootstrap_valid.append(n_boostrap)
    lopbootstrapped_scores_valid.append([])
    rng_seed = 42  # control reproducibility
    loprng_valid = np.random.RandomState(rng_seed)
    for i_bot in range(n_boostrap):
        #print(i_bot)
        indices_validlop = loprng_valid.randint(0, len(Y_Forecast), len(Y_Forecast))
        if len(np.unique(y_valid[indices_validlop])) < 2:
            continue
        lopscore_roauc_valid = roc_auc_score(y_valid[indices_validlop], Y_Forecast[indices_validlop])
        lopbootstrapped_scores_train[i].append(lopscore_roauc_train)
#lopbootstrapped_scores_train      

confidence_lower_lop_valid=[]
confidence_upper_lop_valid=[]
for i in range(len(lopbootstrapped_scores_valid)):
    #rint(i)
    sorted_scores_lop_valid = np.array(lopbootstrapped_scores_train[i])
    sorted_scores_lop_valid.sort()
    confidence_lower_lop_valid.append(round(sorted_scores_lop_valid[int(0.05 * len(sorted_scores_lop_valid))],4))
    confidence_upper_lop_valid.append(round(sorted_scores_lop_valid[int(0.95 * len(sorted_scores_lop_valid))],4))


print(Bold+'Khoảng Tin Cậy 95(%) Của AUROC Qua Các Lần Bootstrap Khác Nhau (Out-Of-Sample)'+End)
print(pd.DataFrame({'Số Bootstrap':Num_bootstrap_valid,
             'Lower Bound':confidence_lower_lop_valid,
             'Upper Bound':confidence_upper_lop_valid}))


# ###  <a href='#out_of19'>Hệ Số Gini (Accuracy Ratio AR) </a>   
# 
# Hệ Số Gini là một trong Hai Hệ Số được sử dụng phổ biến nhất trong Industry. Trong Lĩnh Vực Ngân hàng, Ủy Ban Basel cũng khuyến nghị sử dụng hệ số Gini này và cả hệ số AUC-ROC.
# $$Gini=2*AUC - 1$$

# In[936]:


Gini_valid=[]
for i in range(0,len(roc_results)):
    Gini_valid.append(2*roc_results.at[i,'Diện tích valid']-1)
plt.figure(figsize=(12, 5))
plt.suptitle('Biến động Hệ Số Gini Của Mô Hình Logistic Theo Số Biến Giải Thích \n Out-Of-Sample',
          fontsize=15,fontweight='bold',color='b')
plt.plot(Gini_valid, color='navy', linestyle='-', label='Hệ Số Gini')
plt.xlabel('Số Biến Giải Thích Trong Mô Hình', fontweight='bold',
           color='b',fontsize=12)
plt.ylabel('Hệ Số Gini',fontweight='bold',fontsize=12,color='b')
plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.show()

#plt.figure(figsize=(12, 5))
#sns.distplot(Gini_valid,bins=3, kde=True)
#plt.title('Phân Phối Của Hệ Số Gini')
#plt.autoscale(enable=True, axis='both',tight=True)
#plt.xlabel('Hệ Số Gini', fontsize=12)
#plt.ylabel('Tần Xuất ',fontsize=12)
#plt.show()


# ###  <a href='#out_of191'>Bootstrap for Gini (Accuracy Ratio AR) </a>   

# In[1709]:


bootstrapped_GINI_valid=[(2*p-1) for p in bootstrapped_scores_valid]
plt.figure(figsize=(13, 5))
sns.distplot(bootstrapped_GINI_valid, bins=50, kde=True,hist=True)
plt.suptitle('Distribution of %d Boostrap for GINI (Accuracy Ratio AP) \n (Out-Of-Sample)'%len(bootstrapped_scores_valid),
         fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tần Xuất', fontweight='bold',
           color='b',fontsize=12)
plt.xlabel('Chỉ Số GINI (Accuracy Ratio AP) ',fontweight='bold',fontsize=12,color='b')
plt.show()


# ### <a href='#out_of18'>CAP – Cumulative Accuracy Profile </a>    

# In[963]:


total = len(Y_valid) 
 # Đếm Số Vỡ Nợ Trong Dữ Liệu Kiểm Định     
one_count = np.sum(Y_valid) 
# Đếm Số Không Vỡ Nợ Trong Dữ Liệu Kiểm Định 
zero_count = total - one_count 
  
lm = [y for _, y in sorted(zip(Y_Forecast, Y_valid), reverse = True)] 
x_axis_valid = np.arange(0, total + 1) 
y_axis_valid = np.append([0], np.cumsum(lm)) 


plt.figure(figsize = (10, 6))  
plt.plot([0, total], [0, one_count], c = 'b',  
         linestyle = '-', label = 'Mô Hình Ngẫu Nhiên') 
plt.plot(x_axis_valid, y_axis_valid, c = 'b', label = 'Mô Hình Logistic',
         linestyle = ':',linewidth = 5) 
plt.plot([0, one_count, total], [0, one_count, one_count], linestyle = '-.',
         c = 'grey', linewidth = 2, label = 'Mô Hình Hoàn Hảo') 
plt.suptitle('Phân Tích CAP Của Mô Hình Logistic \n Out-Of-Sample Forecast',
          fontsize=15,fontweight='bold',color='b')
plt.xlabel('Số Người Nợ Ngân Hàng', fontweight='bold',
            color='b',fontsize=12)
plt.ylabel('Số Người Bị Vỡ Nợ Ngân Hàng',fontweight='bold',fontsize=12,color='b')
plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.show()


# ### <a href='#out_of17'>Discriminatory Power Của Mô Hình Logistic </a>   

# In[738]:


target_names = ['Không Xảy Ra Vỡ Nợ', 'Xảy Ra Vỡ Nợ']
print(Bold+'Báo Cáo Khả Năng Phân Loại giữa Xảy Ra Và Không Xảy Ra Vỡ Nợ Của Mô Hình Logistic \n Out-of-Sample'+End)
print(classification_report(Y_valid, Y_Forecast, target_names=target_names))


# ### <a href='#out_of177'>Lorenz Curve Monitoring </a>  

# In[1297]:


Lor_data_valid = zip(Y_valid, Y_Forecast)
sorted_Lor_data_valid = sorted(Lor_data_valid, key=lambda d: d[1])
sorted_Lor_actual_valid = [d[0] for d in sorted_Lor_data_valid]


lorenz_valid = np.cumsum(sorted_Lor_actual_valid) / np.sum(sorted_Lor_actual_valid)
lorenz_valid = np.insert(lorenz_valid, 0, 0) 
lorenz_valid[0], lorenz_valid[-1]

plt.figure(figsize = (10, 6))  
plt.plot(np.arange(lorenz_valid.size)/(lorenz_valid.size-1), lorenz_valid, linestyle = '-.',
            linewidth = 2,color='darkgreen',label='Lorenz Curve ')
plt.plot(np.arange(lorenz.size)/(lorenz.size-1),
         np.arange(lorenz.size)/(lorenz.size-1), 
         linewidth = 1,color='r',label='Line of Equality')
plt.fill_between(np.arange(lorenz.size)/(lorenz.size-1),
                 np.arange(lorenz.size)/(lorenz.size-1), lorenz,
                 color='C1', alpha=0.7,
                 label='Gini Index')

plt.legend(loc="lower right")
plt.autoscale(enable=True,axis='x',tight=True)
plt.suptitle('Đường Cong Lorenz\n Out-Of-Sample Validation',
          fontsize=15,fontweight='bold',color='b')
plt.ylabel('Tỷ Lệ Gía Trị Thực Lũy Tiến \n Cumulative Share of Actual Values',
           fontweight='bold',fontsize=12,color='b')
plt.xlabel('Tỷ Lệ Dự Báo Lũy Tiến \n Cumulative Share of Predictions', fontweight='bold',
            color='b',fontsize=12)
plt.show()


# ### <a href='#out_of178'>Điểm Brier and Calibration Curves </a>  

# In[1572]:


Y_pred_valid = logreg_fitted.predict(X_valid)
Default_Pred_prob_valid = logreg_fitted.predict_proba(X_valid)[:, 1]
NonDef_Pred_prob_valid = logreg_fitted.predict_proba(X_valid)[:, 0]

Default_brier_score_valid=brier_score_loss(Y_valid, Default_Pred_prob_valid, 
                                           pos_label=Y_valid.max())
NonDef_brier_score_valid=brier_score_loss(Y_valid, NonDef_Pred_prob_valid , 
                                           pos_label=Y_valid.max())

fraction_of_default_valid, Default_mean_predicted_value_valid =             calibration_curve(Y_valid, Default_Pred_prob_valid, n_bins=20)
fraction_of_nondefault_valid, NonDef_mean_predicted_value_valid =             calibration_curve(Y_valid, NonDef_Pred_prob_valid, n_bins=20)

fig=plt.figure(figsize=(12,5))
plt.suptitle('Calibration plots  (reliability curve)')
fig.add_subplot(1,2,1)
plt.plot(Default_mean_predicted_value_valid, fraction_of_default_valid, "s-",
                 label="The Brier Score of Logistic Model for Default (%1.3f)" % (Default_brier_score_valid))
plt.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
plt.autoscale(enable=True,axis='x',tight=True)
plt.ylabel("Tỷ Lệ Vỡ Nợ")

plt.xlabel("Gía Trị Xác Xuất Dự Báo Trung Bình Cho Trường Hợp Vỡ Nợ")
plt.legend(loc="upper left")

fig.add_subplot(1,2,2)
plt.plot(NonDef_mean_predicted_value_valid, fraction_of_nondefault_valid, "s-",
                 label="The Brier Score of Logistic Model for NonDefault (%1.3f)" % (NonDef_brier_score_valid))
plt.plot([0, 1], [1, 0], "k:", label="Perfectly calibrated")
plt.autoscale(enable=True,axis='x',tight=True)
plt.ylabel("Tỷ Lệ Không Vỡ Nợ")

plt.xlabel("Gía Trị Dự Báo Trung Bình")
plt.legend(loc="upper left")
plt.show()


# ### <a href='#out_of1799'>The Information Entropy </a>  

# In[1486]:


info_entro_defValid = [-(p*log2(p)) for p in Default_Pred_prob_valid]
fig=plt.figure(figsize=(12,5))
plt.scatter(Default_Pred_prob_valid, info_entro_defValid , marker='.')
plt.title('Xác Xuất Dự Báo Từ Mô Hình Logistic Và Chỉ Số Information Entropy Xảy Ra Vỡ Nợ\n (Out-Of-Sample)',
         fontsize=15,fontweight='bold',color='b')
plt.xlabel('Xác Xuất Dự Báo Từ Mô Hình Logistic',
          fontsize=12,fontweight='bold',color='b')
plt.ylabel('Chỉ Số Information Entropy',
          fontsize=12,fontweight='bold',color='b')
plt.show()


# ### <a href='#out_of179'>Precision-Recall Curve </a>  

# In[1352]:


average_precision_valid = average_precision_score(Y_valid, Y_Forecast)  
disp = plot_precision_recall_curve(logreg_fitted, X_valid, Y_valid)
disp.ax_.set_title('2-class Precision-Recall curve\n Out-of-sample \n AP={0:0.2f}'.format(average_precision_valid))
plt.show()


# ### <a href='#out_of3'>Sự Ổn Định Của Logistic </a>    

# In[733]:


scoring = 'accuracy'
training_time = []
num_train=50
kfold = KFold(n_splits=num_train, random_state=7,shuffle=True)
start = timer()
print(Red+'Bạn Vui Lòng chờ tý. Tôi sẽ làm xong ngay đây...!'+End)
model=LogisticRegression(solver='liblinear',
                                            penalty='l1',fit_intercept=False)
cv_results_Logit = cross_val_score(model, X_train,Y_train,
                                   cv=kfold, scoring=scoring)
print(Red+'Ok, Tôi đã ước lượng Mô Hình Logistic  %d lần khác nhau trong %.2f giây'%       (num_train,timer() - start)+End)
print(Red+'Dưới đây là kết quả kiểm tra qua  %d lần ước lượng'%      num_train+End)
fig = plt.figure(figsize=(10,4))
sns.distplot(cv_results_Logit,bins=20, kde=True)
plt.title('Sự Ổn Định Của Mô Hình Logistic Qua  %d Lần Ước Lượng Lại'%      num_train,fontsize=14,fontweight='bold')
plt.autoscale(enable=True, axis='both',tight=True)
plt.xlabel('Chỉ Số Accuracy', fontsize=12)
plt.ylabel('Số Lần ',fontsize=12)
plt.show()

fig = plt.figure(figsize=(10,4))
plt.boxplot(cv_results_Logit,vert=False, showmeans=True)  
plt.autoscale(enable=True, axis='x',tight=True)
plt.xlabel('Chỉ Số Accuracy', fontsize=12)
#plt.ylabel('Số Lần ',fontsize=12)
plt.show()


# ### <a href='#out_sample793'>Xác Xuất Vỡ Nợ (PD) Và Tỷ Lệ Duyệt Khoản Vay</a> 

# In[1574]:


threshold_accepted_train = np.quantile(Default_Pred_prob_train, 0.85)
fig=plt.figure(figsize=(12,5))
plt.suptitle('Dự Báo Xác Xuất Xảy Ra Vỡ Nợ (PD) Từ Mô Hình Logistic và Ngưỡng Duyệt Một Khoản Vay \n (Out-Of-Sample Forecast)')
sns.distplot(Default_Pred_prob_valid,hist=True,rug=False,
             kde_kws={'linestyle':'--'},label='PD Ước Lượng')
plt.axvline(threshold_accepted_train,lw='3',color='r')#,
            #label='Gía Trị Ngưỡng Một Khoản Vay Được Duyệt')
plt.annotate('\n Gía Trị Ngưỡng (%.2f) \n Một Khoản Vay \n Được Duyệt'%threshold_accepted_train, 
             xy=(0.66, 4.2), xytext=(0.7, 4),
           arrowprops=dict(facecolor='r', shrink=0.01))

plt.ylabel("Tần Xuất")

plt.xlabel("The Out-Of-Sample Probability of Default (PD)")
plt.legend(loc="lower left")
plt.show()


# ###  <a href='#Valid_13'>So Sánh Độ Nhạy Của Mô Hình Logistic với các Model khác  </a> 

# In[566]:


models = []
models.append(('RidgeClass', RidgeClassifier()))
#models.append(('LinearSVC', LinearSVC()))
models.append(('SGDClass', SGDClassifier()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('NearCent',NearestCentroid()))
#models.append(('Logit',LogisticRegression()))
models.append(('Logit',LogisticRegression(solver='liblinear',
                                            penalty='l1',fit_intercept=False)))

competing_model_score = []
results = []
names = []
print(Red+"Xin Vui lòng Đợi Tý.....")
for name, model in models:
    scoring = 'accuracy'
    training_time = []
    kfold = KFold(n_splits=10, random_state=7,shuffle=True)
    start = timer()
    cv_results = cross_val_score(model, X_train,Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    training_time.append(timer() - start)
    val = [name, cv_results.mean(), cv_results.std(),sum(training_time)]
    competing_model_score.append(val)
    #msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    #print(msg) 
print(Blue+"Tôi làm xong rồi đấy.Chạy dòng lệnh tiếp theo mà in kết quả ra đi")

compared_results1 = pd.DataFrame(competing_model_score,)
compared_results1.columns = ['Mô hình', 'Điểm Bình Quân',
                         'Sai Số Chuẩn', 'Thời gian đào tạo (s)']
print(Bold+'Kết quả so sánh Độ Nhạy của %d Mô Hình khác nhau trong dự báo:'%(len(models))+End)
print(compared_results1)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
plt.boxplot(results,vert=False, showmeans=True)  
ax.set_yticklabels(names)
plt.grid(which='major',linestyle=':',linewidth=0.9)
plt.title('Biến Động Của Chỉ Số Accuracy của %d Mô Hình khác nhau'%len(models),
          fontsize=14,fontweight='bold')
plt.ylabel('Tên %d Mô Hình'%(len(models)), fontsize=11)
plt.xlabel('Phân phối của Khả Năng Dự Báo Chính Xác (Accuracy) qua 10 Lần ước lượng', fontsize=11)
plt.show()


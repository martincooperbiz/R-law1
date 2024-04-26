
import streamlit as st
import pandas as pd

# Hardcoded CSV file path
CSV_FILE_PATH = "2.csv"


# Dictionary mapping categories to their associated keywords
keywords_by_category = {
'قانون العقود والالتزامات': ['عقود', 'اتفاقيات', 'إيجار', 'بيع', 'شراء', 'مقاولة', 'تفويت', 'رهن', 'كفالة', 'تعويضات', 'التزامات', 'عقد', 'فسخ', 'إبطال', 'تنفيذ', 'تفسير', 'شروط', 'التزام', 'أداء', 'مبيع', 'مشتري', 'بائع'],
'قانون المسؤولية التقصيرية': ['تعويضات', 'نزاعات', 'إصابات', 'أضرار', 'خطأ', 'مسؤولية', 'تقصير', 'إهمال', 'حوادث', 'جبر ضرر'],
'قانون الأسرة': ['زواج', 'طلاق', 'نفقة', 'حضانة', 'أطفال', 'تبني', 'ولاية', 'وصاية', 'أحوال', 'أسرة', 'علاقة زوجية', 'خلع', 'تعدد الزوجات', 'عنف', 'قرابة', 'مصاهرة', 'نسب', 'إقرار بالنسب', 'بنوة', 'أبوة', 'إثبات النسب'],
'قانون المواريث': ['إرث', 'تركات', 'مواريث', 'وصايا', 'هبات', 'أوقاف', 'توريث', 'ميراث', 'قسمة', 'توزيع', 'إحصاء', 'تخارج'],
'قانون الشركات والتجارة': ['معاملات', 'شراكات', 'شركات', 'إفلاس', 'ملكية', 'تجارة', 'بيع', 'شراء', 'استيراد', 'تصدير', 'سندات', 'أسهم', 'ملكية فكرية', 'ملكية تجارية', 'مسؤولية الشركاء', 'تصفية', 'شيكات', 'أوراق تجارية'],
'قانون الإدارة': ['لوائح', 'هيئات', 'إجراءات', 'رقابة', 'قرارات', 'مراسيم', 'أنظمة', 'استشارات', 'طعون', 'إدارية', 'حكومية', 'قضائية', 'تجاوز السلطة', 'اختصاص', 'مشروعية', 'إلغاء قرار إداري'],
'قانون الشغل والضمان الاجتماعي': ['عقود', 'سلامة', 'أمن', 'تعويضات', 'نقابات', 'تمييز', 'تحرش', 'ساعات', 'إجازات', 'رواتب', 'عمل', 'عمالية', 'وظيفي', 'فصل تعسفي', 'حوادث شغل', 'ضمان اجتماعي', 'تعويضات عائلية', 'تقاعد', 'شيخوخة', 'عجز'],
'قانون العقارات والملكية العقارية': ['ملكية', 'تعاملات', 'تنظيم', 'نزاعات', 'رهون', 'إخلاء', 'تسجيل', 'تخطيط', 'عقارية', 'مالك', 'مستأجر', 'استخدام', 'أراضي', 'عمراني', 'تحفيظ', 'ملك', 'حيازة', 'تصرف', 'قسمة', 'شفعة', 'بيع بالمزاد', 'جوار', 'ارتفاق'],
'القانون الجنائي': ['جنايات', 'جنح', 'مخالفات', 'إجراءات', 'عقوبات', 'استئناف', 'إثبات', 'جرائم إلكترونية', 'قصد', 'أهلية', 'شروع', 'جرائم', 'جنائية', 'جنائي', 'تلبس', 'سرقة', 'نصب', 'تبديد', 'قتل', 'ضرب', 'جرح', 'تهديد', 'فساد', 'مخدرات', 'تزوير', 'خيانة الأمانة'],
'قانون البيئة': ['تلوث', 'موارد', 'حماية', 'تقييم', 'لوائح', 'مخلفات', 'نفايات', 'انبعاثات', 'مناخ', 'كوارث', 'بيئة', 'بيئي', 'طبيعية', 'تنمية مستدامة', 'تغير مناخي', 'تلوث الهواء', 'تلوث المياه', 'تلوث التربة', 'المسؤولية البيئية'],
'القانون الدستوري': ['حقوق', 'حريات', 'فصل السلطات', 'رقابة', 'تفسير', 'ديمقراطية', 'انتخابات', 'حكم', 'مؤسسات', 'لامركزية', 'أساسية', 'مدنية', 'سلطات', 'دستوري', 'حكومة', 'برلمان', 'قضاء', 'سيادة', 'مواطنة']
}

# Function to retrieve legal texts containing keywords for the given categories and keywords
def retrieve_texts_by_categories_and_keywords(categories, keywords, num_rows_to_retrieve, csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Initialize a list to store rows containing the keywords
    keyword_rows = []

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Initialize a set to store the unique category keywords present in the row
        row_keywords = set()

        # Initialize a variable to store the full text of the row
        full_text = ""

        # Initialize a flag to track if the row contains any keyword
        row_contains_keyword = False

        # Iterate over each cell in the row
        for cell in row:
            # Check if the cell contains any of the keywords for the selected categories
            if isinstance(cell, str):
                for category in categories:
                    for keyword in keywords_by_category.get(category, []):
                        if keyword in cell:
                            # Add the keyword to the row_keywords set (to avoid duplicates)
                            row_keywords.add(keyword)
                            row_contains_keyword = True

        # If the row contains any keyword, append the entire row to the full_text
        if row_contains_keyword:
            for cell in row:
                if isinstance(cell, str):
                    full_text += f"{cell} "

        # Calculate the unique keyword count for the row
        unique_keyword_count = len(row_keywords)

        # If the row contains any of the keywords, append it to the keyword_rows list
        if unique_keyword_count > 0 and any(keyword in row_keywords for keyword in keywords):
            word_count = len(full_text.split())
            row_dict = {
                'رقم الملف': row['رقم الملف'],
                'رقم القرار': row['رقم القرار'],
                'تاريخ القرار': row['تاريخ القرار'],
                'القاعدة القانونية': full_text.strip(),
                'تحميل القرار': row['تحميل القرار'],
                'عدد الكلمات المفتاحية الفريدة': unique_keyword_count,
                'الكلمات المفتاحية': ', '.join(row_keywords)
            }
            keyword_rows.append(row_dict)

    # Sort the rows based on the unique keyword count in descending order
    if keyword_rows:
        keyword_rows.sort(key=lambda x: x['عدد الكلمات المفتاحية الفريدة'], reverse=True)

        # Select the top rows based on the user's input
        top_rows = keyword_rows[:int(num_rows_to_retrieve)]
    else:
        top_rows = []

    return top_rows

# Main function for Streamlit app
def main():
    st.title('Legal Text Retrieval App')

    # Select categories
    selected_categories = st.multiselect("Select categories", list(keywords_by_category.keys()))

    # Create a dropdown for each selected category to select keywords
    selected_keywords = []
    for category in selected_categories:
        category_keywords = keywords_by_category[category]
        selected_keywords_for_category = st.multiselect(f"Select keywords for {category}", category_keywords)
        selected_keywords.extend(selected_keywords_for_category)

    # Allow user to select the number of rows to retrieve
    num_rows_to_retrieve = st.number_input("Number of rows to retrieve", min_value=1, max_value=1000, value=100, step=1)

     # Retrieve texts for the selected categories and keywords
    if selected_categories and selected_keywords:
        selected_texts = retrieve_texts_by_categories_and_keywords(selected_categories, selected_keywords, num_rows_to_retrieve, CSV_FILE_PATH)

        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(selected_texts)

        # Calculate the total word count
        if not df.empty:
            total_word_count = df['القاعدة القانونية'].apply(lambda x: len(str(x).split())).sum()
        else:
            total_word_count = 0

        # Display the total word count
        st.subheader("Total Word Count")
        st.write(total_word_count)

        # Write the DataFrame to a CSV file
        df.to_csv('output.csv', index=False)

        # Create a DataFrame for the extracted data
        extracted_data_df = pd.DataFrame([
            f"File Number: {row['رقم الملف']}\nDecision Number: {row['رقم القرار']}\nDecision Date: {row['تاريخ القرار']}\nLegal Basis:\n{row['القاعدة القانونية']}\nKeywords Present: {row['الكلمات المفتاحية']}\n[القرار]({row['تحميل القرار']})\n\n"
            for _, row in df.iterrows()
        ], columns=['Data'])

        # Create a data editor for the extracted data
        edited_data_df = st.data_editor(extracted_data_df, use_container_width=True)

        # Concatenate all extracted data into a single string
        extracted_data_str = "\n\n".join(extracted_data_df['Data'].tolist())

        # Create a copy button to copy the extracted data
        st.markdown("### Copy Extracted Data")
        copy_button = st.button("Copy to Clipboard")
        if copy_button:
            st.write("Copied to clipboard!")
            st.code(extracted_data_str, language="text")

        # Display the data
        st.subheader(f"Texts for Categories: {', '.join(selected_categories)}")
        for index, row in df.iterrows():
            st.subheader(f"File Number: {row['رقم الملف']}")
            st.subheader(f"Decision Number: {row['رقم القرار']}")
            st.subheader(f"Decision Date: {row['تاريخ القرار']}")
            st.write(f"**Legal Basis:**")
            st.write(row['القاعدة القانونية'])  # Display the full text
            st.write(f"**Keywords Present:** {row['الكلمات المفتاحية']}")  # Display the keywords present
            st.write(f"[القرار]({row['تحميل القرار']})")
            st.write("---")

        # Display the total word count
        st.subheader("Total Word Count")
        st.write(total_word_count)
    else:
        st.warning("Please select at least one category and at least one keyword.")

if __name__ == "__main__":
    main()

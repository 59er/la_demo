import streamlit as st
import streamlit.components.v1 as stc 
from eng_edu_overview_app import run_edu_overview_app
from eng_edu_detail_app import run_edu_detail_app
from eng_test_cronbach_alpha_app import run_test_cronbach_alpha_app
from eng_edu_score_prediction_app import run_edu_score_prediction_app
from eng_edu_pass_fail_prediction_app import run_edu_pass_fail_prediction_app
from eng_cluster_app import run_cluster_app
from eng_corr_app import run_corr_app
from eng_text_mining_app import run_text_mining_app
from eng_test_difficulty_app import run_test_difficulty_app
from eng_t_test_app import run_t_test_app
from eng_factor_app import run_factor_app
from eng_time_analysis_app import run_time_analysis_app
from eng_edu_score_prediction_app import run_edu_score_prediction_app
from eng_course_recommend_app import run_course_recommend_app
from eng_sampling_adequacy_app import run_sampling_adequacy_app

def main():
    st.title("教育データ分析WEB (β version)")

    menu = ["HOME",'クラス別分析','詳細分析',
            '相関分析',
            '得点予測',
            '合否予測','アンケートテキスト分析',
            'テスト・アンケートの信頼性測定','テスト難易度と識別力分析',
            'クラスター分析','t検定','サンプルサイズ妥当性測定','因子分析','時系列分析','コースレコメンド']
 
    choice = st.sidebar.selectbox("MENU",menu)
    st.sidebar.text('Select a function from the MENU.')

    # choice = st.sidebar.selectbox("Menu",menu)

    if choice =='HOME':
        st.header("■分析メニュー")
        st.write('The following learning analysis can be selected from the sidebar menu.')
        # st.subheader('Menu')
        st.subheader('- クラス別分析:')
        st.write(' To get an overview of the test results. To understand the trend of each class visually.')
        st.subheader('- 詳細分析: ')
        st.write('To investigate the relationship between learning time and academic achievement.')
        st.subheader('- 相関分析: ')
        st.write('To investigate the relationship between midterm and final exam grades.')
        st.subheader('- 得点予測: ')
        st.write(' To predict the expected score of students who are absent from the test.')
        st.subheader('- 合否予測: ')
        st.write('To know what makes students pass or fail.')
        st.subheader('- アンケートテキスト分析:')
        st.write(' To analyze the free text of the class evaluation questionnaire.')
        st.subheader('- テスト・アンケートの信頼性測定: ')
        st.write('To measure the validity and reliability of tests.')
        st.subheader('- テスト難易度と識別力分析:')
        st.write(' To grade each test based on its difficulty and discrimination.')
        st.subheader('- クラスター分析: ')
        st.write('To group students who have similar learning characteristics.')
        st.subheader('- t検定: ')
        st.write('To compare the results of two tests. e.g., examine the difference in performance by teaching method.')
        st.subheader('サンプルサイズ妥当性測定')
        st.write('To investigate the adequay of the number of samples for questionnaire.')
        st.subheader('- 因子分析: ')
        st.write('To create and analyze a class evaluation questionnaire.')
        st.subheader("- 時系列分析:")
        st.write( "To visualize the academic achievement over time.")
        st.subheader("- コースレコメンド")
        st.write("To recommend optimal study course for learners")
        
    elif choice == "クラス別分析":
        # run_overview_app()
        run_edu_overview_app()

    elif choice == "詳細分析":
        run_edu_detail_app()

    elif choice == "相関分析":
        run_corr_app()

    elif choice == "得点予測":
        run_edu_score_prediction_app()

    elif choice == "合否予測":
        run_edu_pass_fail_prediction_app()

    elif choice == "アンケートテキスト分析":
        run_text_mining_app()

    elif choice == "テスト・アンケートの信頼性測定":
        run_test_cronbach_alpha_app()

    elif choice == 'テスト難易度と識別力分析':
        run_test_difficulty_app()
        
    elif choice == "サンプルサイズ妥当性測定":
        run_sampling_adequacy_app()

    elif choice == "クラスター分析":
        run_cluster_app()

    elif choice == "t検定":
        run_t_test_app()

    elif choice == "因子分析":
        run_factor_app()

    elif choice == '時系列分析':
        run_time_analysis_app()

    elif choice == 'コースレコメンド':
        run_course_recommend_app()

if __name__ == '__main__':
    main()

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

    menu = ["HOME",'教科別・クラス別成績分析','詳細分析',
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
        st.write('左サイドメニューから機能を選択してください。')
        # st.subheader('Menu')
        st.subheader('- 教科別・クラス別成績分析:')
        st.write(' テスト結果の概要を知りたい.クラスごとの傾向を視覚的に把握したい.')
        st.subheader('- 詳細分析: ')
        st.write('学習時間と学力との関係を調べたい.')
        st.subheader('- 相関分析: ')
        st.write('中間試験と期末試験の成績の関係を調べたい.')
        st.subheader('- 得点予測: ')
        st.write(' 成績データから将来を予測したい.テスト欠席者の見込み点を予測したい.')
        st.subheader('- 合否予測: ')
        st.write('合格・不合格の要因を知りたい.')
        st.subheader('- アンケートテキスト分析:')
        st.write(' 授業評価アンケートの自由記述を分析したい.')
        st.subheader('- テスト・アンケートの信頼性測定: ')
        st.write('テストの妥当性と信頼性を測定したい.')
        st.subheader('- テスト難易度と識別力分析:')
        st.write(' テストごとの難易度・識別力を考慮して成績をつけたい.')
        st.subheader('- クラスター分析: ')
        st.write('同じような特徴を持つ学生をグループ化したい.')
        st.subheader('- t検定: ')
        st.write('２つのグループのテスト結果を比較したい、指導法による成績の違いを調べたい.')
        st.subheader('サンプルサイズ妥当性測定')
        st.write('アンケートのサンプル数の妥当性を測定したい.')
        st.subheader('- 因子分析: ')
        st.write('授業評価アンケートを作成・分析したい.')
        st.subheader("- 時系列分析:")
        st.write( "学力を時系列に俯瞰したい.")
        st.subheader("- コースレコメンド")
        st.write("生徒のレベルに合った最適なコースを推奨したい.")
        
    elif choice == "教科別・クラス別成績分析":
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

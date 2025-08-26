
from scripts.o1_preprocessing import preprocess_sales_data
from scripts.o2_analysis_and_viz import analyze_and_visualize_updated


def run_pipeline():
    print('--- Running Sales Analysis Pipeline ---')
    
    # Step 1: Preprocessing
    preprocess_sales_data()
    
    # Step 2: Analysis & Visualization
    analyze_and_visualize_updated()

    print('--- Pipeline Execution Complete ---')


if __name__ == '__main__':
    run_pipeline()

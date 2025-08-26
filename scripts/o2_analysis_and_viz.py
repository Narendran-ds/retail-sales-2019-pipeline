import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def analyze_and_visualize_updated():
    """
    Loads cleaned sales data and generates five advanced visualizations,
    including a Waterfall Chart and a 3D Scatter Plot.
    """
    print("\n--- Starting Analysis & Visualization ---")

    # Define paths
    sales_path = os.path.join('01_data', 'processed', 'cleaned_sales.parquet')
    viz_dir = '03_visualizations_final'
    os.makedirs(viz_dir, exist_ok=True)

    # Load Data
    try:
        df = pd.read_parquet(sales_path)
    except FileNotFoundError:
        print(f"Error: Processed data not found at '{sales_path}'.")
        return
        
    print("\n--- Generating 5 Final Visualizations ---")

    # Visualization 1: Correlation Heatmap
    corr_df = df[['Quantity Ordered', 'Price Each', 'Hour', 'Sales']]
    corr_matrix = corr_df.corr()
    fig1 = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                     color_continuous_scale='RdBu_r',
                     title='<b>1. Correlation Matrix of Key Numeric Features</b>')
    fig1.write_image(os.path.join(viz_dir, "01_correlation_heatmap.png"), width=800, height=600)
    print("1/5 Saved: Correlation Heatmap")

    # Visualization 2: Violin Plot
    product_qty = df.groupby('Product')['Quantity Ordered'].sum()
    top_5_products = product_qty.nlargest(5).index
    violin_data = df[df['Product'].isin(top_5_products)]
    fig2 = px.violin(violin_data, x='Product', y='Sales', color='Product',
                     box=True, points=False,
                     title='<b>2. Sales Value Distribution for Top 5 Products</b>')
    fig2.write_image(os.path.join(viz_dir, "02_sales_violin_plot.png"), width=1200, height=700)
    print("2/5 Saved: Sales Distribution Violin Plot")

    # Visualization 3: Choropleth Map
    df['State'] = df['City'].apply(lambda x: x.split('(')[-1].replace(')', ''))
    state_sales = df.groupby('State')['Sales'].sum().reset_index()
    fig3 = px.choropleth(state_sales, locations='State', locationmode="USA-states",
                        color='Sales', scope="usa", color_continuous_scale="Viridis",
                        title='<b>3. Total Sales Revenue by State</b>')
    fig3.write_image(os.path.join(viz_dir, "03_sales_choropleth_map.png"), width=1000, height=600)
    print("3/5 Saved: Choropleth Map")

    # Visualization 4: Waterfall Chart
    city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False)
    fig4 = go.Figure(go.Waterfall(
        name="Sales", orientation="v",
        measure=["relative"] * len(city_sales) + ["total"],
        x=list(city_sales.index) + ["Total"],
        y=list(city_sales.values) + [city_sales.sum()],
        text=[f"${v/1000:.1f}k" for v in city_sales.values] + [f"${city_sales.sum()/1000:.1f}k"],
        textposition="outside",
    ))
    fig4.update_layout(title="<b>4. How City Sales Contribute to Total Revenue</b>",
                       showlegend=False, yaxis_title="Sales (USD)")
    fig4.write_image(os.path.join(viz_dir, "04_sales_waterfall.png"), width=1200, height=700)
    print("4/5 Saved: Sales Contribution Waterfall Chart")
    
    # Visualization 5: 3D Scatter Plot
    sample_df = df.sample(n=2000, random_state=42)
    fig5 = px.scatter_3d(sample_df, x='Price Each', y='Quantity Ordered', z='Hour',
                        color='Sales', title='<b>5. 3D View: Price vs. Quantity vs. Hour</b>',
                        color_continuous_scale='Plasma')
    fig5.write_image(os.path.join(viz_dir, "05_3d_sales_scatter.png"), width=1200, height=800)
    print("5/5 Saved: 3D Sales Scatter Plot")

    print("\n--- Final Analysis and Visualization Complete! ---")

if __name__ == '__main__':
    analyze_and_visualize_updated()

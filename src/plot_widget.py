from PyQt6.QtWebEngineWidgets import QWebEngineView
import plotly.express as px
import pandas as pd

class PlotWidget(QWebEngineView):
    def set_data(self, df: pd.DataFrame):
        fig = px.line(df, x="created_at", y="value", title="Measurements")
        html = fig.to_html(include_plotlyjs="cdn")
        self.setHtml(html)
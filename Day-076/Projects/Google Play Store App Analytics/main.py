df_paid_apps = df_apps_clean[df_apps_clean["Type"] == "Paid"]
box = px.box(
    df_paid_apps,
    x="Category",
    y="Revenue_Estimate",
    title="How Much Can Paid Apps Earn?",
)

box.update_layout(
    xaxis_title="Category",
    yaxis_title="Paid App Ballpark Revenue",
    xaxis={"categoryorder": "min ascending"},
    yaxis=dict(type="log"),
)


box.show()

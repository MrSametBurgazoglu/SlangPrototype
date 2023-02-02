func button_clicked():
    print("button clicked")


component Button:
    Button(text):
        change_text("text_widget", text)
    {
        Widget:MouseButtonInput
        .connect("button_clicked", button_clicked)
        {
            TextWidget:
            .set_name("text_widget")
        }
    }

MainWidget:
.set_width("500px")
.set_height("400px")
{
    Box:MouseButtonInput
    .set_vertical_align("center")
    .set_horizontal_align("center")
    .set_position("50px", "50px")
    ./MouseButtonInput.connect("button_clicked", button_clicked)
    {
        ColorRect:
        .set_color("gray")
        .set_width("100%")
        .set_height("100%")
        TextWidget:
        .set_text("First Button")
    }
    component Button("new button from component"):
}
func button_clicked():
    print("button clicked")
    change_property("text_widget", "text", "changed text")

component Button:
    Button(text):
        change_property("text_widget", "text", text)
    {
        Widget:MouseButtonInput
        ./MouseButtonInput.connect("button_clicked", $button_clicked)
        .set_width("50px")
        .set_height("50px")
        {
            TextWidget:
            .set_name("text_widget")
        }
    }

MainWidget:
    .set_width("500px")
    .set_height("400px")
    {
    ColorRect:
        .set_color("gray")
        .set_position("25%", "10%")
        .set_width("50%")
        .set_height("80%")
        {
        Box:
            .set_vertical_align("center")
            .set_horizontal_align("center")
            .set_width("100%")
            .set_height("100%")
            .set_orientation("vertical")
            .set_spacing("20")
            {
            ImageRect:
                .set_source("example.png")
            ColorRect:
                .set_color("white")
                .set_width("50%")
                .set_height("max-content")
                {
                Box:
                    .set_width("100%")
                    .set_height("max-content")
                    {
                    TextWidget:
                        .set_text("hello")
                    }
                }
            ColorRect:
                .set_color("blue")
                .set_width("50%")
                .set_height("max-content")
                {
                Box:MouseButtonInput
                    .set_width("100%")
                    .set_height("max-content")
                    ./MouseButtonInput.connect("button_clicked", $button_clicked)
                    {
                    TextWidget:
                        .set_text("hello")
                        .set_name("text_widget")
                    }
                }
            }
        }
    }
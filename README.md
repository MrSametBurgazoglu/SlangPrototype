# SlangPrototype
Slang Prototype

Front-End language works in SlangEngine

```
func button_clicked():
    print("button clicked")

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
        .set_position("50px", "50px")
        .set_width("max-content")
        .set_height("80%")
        {
        Box:MouseButtonInput
            .set_vertical_align("center")
            .set_horizontal_align("center")
            .set_width("max-content")
            .set_height("100%")
            .set_orientation("vertical")
            ./MouseButtonInput.connect("button_clicked", $button_clicked)
            {
                TextWidget:
                .set_text("First Button")
                .set_color("red")
                ImageRect:
                .set_source("example.png")
            }
        }
    }
```

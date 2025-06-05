function handle_dragbar(event, self) {
    [l_display, r_display] = self.dependencies
    event_type = event.type

    if (event_type == "mousedown") {
        self.focused = true
        self.display.width += 10
        self.display.offset_x -= 5

        self.mousemove = () => {
            self.display.offset_x = MOUSE.x - self.display.width / 2

            l_display.width = self.display.offset_x + self.display.width / 2
            r_display.offset_x = l_display.width
            r_display.width = window.innerWidth - l_display.width
        }

        window.addEventListener("mousemove", self.mousemove)
        console.log("mousedown", self.display.width)
    }
    else if (event_type == "mouseup") {
        if (self.focused) {
            self.display.width -= 10
            self.display.offset_x += 5
        }
        self.focused = false


        window.removeEventListener("mousemove", self.mousemove)
        console.log("mouseup", self.display.width)
    }

    // console.log(self.display)
    // console.log("skibidi inside_dragbar")
}
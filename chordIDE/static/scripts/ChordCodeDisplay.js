class ChordCodeDisplay {
    constructor(display, line_height) {
        this.display = display

        this.focused_line = null
        this.line_height = line_height
        this.max_visible_lines = Math.floor(this.display.height / this.line_height)

        this.line_text_map = new Map()
    }

    get_line_from_mouse_pos(y) {
        let h_step = this.display.height / this.max_visible_lines
        let line = Math.ceil(y / h_step) - 1

        console.log(y, line)
        return line
    }

    render(ctx) {
        let h_step = this.display.height / this.max_visible_lines
        for (let i = 0; i < this.max_visible_lines; i++) {
            if (this.focused_line != null && this.focused_line == i) {
                ctx.fillStyle = "#222831"
            }
            else ctx.fillStyle = this.display.color
            console.log(this.display.offset_x, h_step, this.display.width)
            ctx.fillRect(this.display.offset_x, i * h_step, this.display.width, h_step)

            if (this.line_text_map.get(i)) {
                ctx.font = `${this.line_height - 10}px Arial`;
                ctx.fillStyle = "#bbccdd"
                ctx.fillText(this.line_text_map.get(i), this.display.offset_x + 10, i * h_step - h_step / 4);
                // ctx.strokeStyle = "#002222"
                // ctx.strokeText(this.line_text_map.get(i), this.display.offset_x + 10, i * h_step - h_step / 4);
            }
        }

        for (let i = 1; i < this.max_visible_lines; i++) {
            ctx.fillStyle = "#393E46"
            ctx.fillRect(this.display.offset_x, i * h_step, this.display.width, h_step / 30)
        }
    }
}


function set_focused_line(event, self) {
    let line = self.display_derivative.get_line_from_mouse_pos(event.y)
    self.display_derivative.focused_line = line

    console.log(line, self.display_derivative.focused_line, self)
}

function input_text(event, self) {
    let keycode = event.e.key
    let line = self.display_derivative.focused_line + 1
    if (!line) return
    let text = self.display_derivative.line_text_map.get(line)
    console.log(text, "mreow", line)
    if (!text) self.display_derivative.line_text_map.set(line, keycode)
    else self.display_derivative.line_text_map.set(line, text + keycode)
    console.log(self.display_derivative.line_text_map.get(line), keycode)
}
class ChordCodeDisplay {
    constructor(display, line_height) {
        this.display = display

        this.focused_line = null
        this.line_height = line_height
        this.max_visible_lines = Math.floor(this.display.height / this.line_height)
        this.ptr = 0

        this.font_size = this.line_height - 10
        this.line_text_map = new Map()
    }

    get_line_from_mouse_pos(y) {
        let h_step = this.display.height / this.max_visible_lines
        let line = Math.floor(y / h_step)

        console.log(y, line)
        return line
    }

    line_to_text(line) {
        return (this.line_text_map.get(line)) ? this.line_text_map.get(line).join('') : ""
    }

    get_chord_code() {
        let text = ""
        for (let i = 0; i < this.max_visible_lines; i++) {
            text += this.line_to_text(i) + " "
        }
        return text
    }

    render(ctx) {
        let h_step = this.display.height / this.max_visible_lines
        let ptr_y = 0
        for (let i = 0; i < this.max_visible_lines; i++) {
            if (this.focused_line != null && this.focused_line == i) {
                ctx.fillStyle = "#222831"
                ptr_y = i * h_step + h_step / 8
            }
            else ctx.fillStyle = this.display.color
            // console.log(this.display.offset_x, h_step, this.display.width)
            ctx.fillRect(this.display.offset_x, i * h_step, this.display.width, h_step)

            if (this.line_text_map.get(i)) {
                ctx.font = `${this.font_size}px monospace`;
                ctx.fillStyle = "#bbccdd"
                ctx.fillText(this.line_to_text(i), this.display.offset_x + 10, (i + 1) * h_step - h_step / 4);
                // ctx.strokeStyle = "#002222"
                // ctx.strokeText(this.line_text_map.get(i), this.display.offset_x + 10, i * h_step - h_step / 4);
            }
        }

        for (let i = 1; i < this.max_visible_lines; i++) {
            ctx.fillStyle = "#393E46"
            ctx.fillRect(this.display.offset_x, i * h_step, this.display.width, h_step / 30)
        }

        if (this.focused_line != null) this.render_ptr(ctx, ptr_y)
    }

    render_ptr(ctx, ptr_y) {
        // console.log(this.line_text_map)
        let len = 1
        if (this.line_text_map.get(this.focused_line)) len = this.line_text_map.get(this.focused_line).length

        let x = this.ptr * ctx.measureText(this.line_to_text(this.focused_line)).width / len || 0
        ctx.fillStyle = "#f60b59"
        // console.log(len, this.ptr, x, ptr_y, ctx.measureText(this.line_to_text(this.focused_line)).width, this.line_to_text(this.focused_line))
        ctx.fillRect(this.display.offset_x + x + 8, ptr_y, 2, this.font_size)

    }
}


function set_focused_line(event, self) {
    let line = self.display_derivative.get_line_from_mouse_pos(event.y)
    self.display_derivative.focused_line = line

    if (event.type == "mousedown") self.display_derivative.ptr = 0
    console.log(line, self.display_derivative.focused_line, self)
}

function input_text(event, self) {
    self = self.display_derivative
    let keycode = event.e.key
    let is_ctrl_active = event.e.ctrlKey
    let is_shift_active = event.e.shiftKey
    console.log(keycode, is_ctrl_active, is_shift_active)

    if (self.focused_line === null) return
    if (keycode.length > 1) {
        if (keycode == "Backspace" && self.line_to_text(self.focused_line).length > 0 && self.ptr > 0) {
            self.line_text_map.get(self.focused_line).splice(self.ptr - 1, 1)
            self.ptr = (self.ptr > 0) ? self.ptr - 1 : self.ptr
        }
        else if (keycode == "Delete" && self.line_to_text(self.focused_line).length > 0) {
            self.line_text_map.get(self.focused_line).splice(self.ptr, 1)
        }

        else if (keycode == "ArrowUp" && self.focused_line > 0) {
            self.focused_line -= 1
            self.ptr = 0
        }
        else if (keycode == "Enter" && is_shift_active) {
            Net.playback(self.get_chord_code())
            return
        }
        else if (["ArrowDown", "Enter"].includes(keycode) && self.focused_line < self.max_visible_lines - 1) {
            self.focused_line += 1
            self.ptr = 0
        }
        else if ("ArrowLeft" == keycode) self.ptr = (self.ptr > 0) ? self.ptr - 1 : self.ptr
        else if ("ArrowRight" == keycode) self.ptr = (self.ptr < self.line_to_text(self.focused_line).length) ? self.ptr + 1 : self.ptr
        else if ("Escape" == keycode) {
            self.focused_line = null
            self.ptr = 0
        }
        console.log(keycode, self.focused_line)
    }
    else {
        if (keycode == "=") {
            Net.eval_chord_code(self.get_chord_code())
            return
        }
        if (keycode.toLowerCase() == "v" && is_ctrl_active) {
            navigator.clipboard.readText().then((text) => {
                console.log(text)
                let split = text.split("\n")
                for (let line of split) {
                    for (let char of line.trim()) {
                        insert_char(self, char)
                    }
                    if (self.focused_line < self.max_visible_lines - 1) {
                        self.focused_line += 1
                        self.ptr = 0
                    }
                }
            })
        }
        else {
            insert_char(self, keycode)
        }
        // console.log(text, "mreow", self.focused_line)
    }

    // console.log(self.display_derivative.line_text_map.get(line), keycode)
}

function insert_char(self, keycode) {
    let text = self.line_text_map.get(self.focused_line)
    if (!text) self.line_text_map.set(self.focused_line, [keycode])
    else text.splice(self.ptr, 0, keycode)
    self.ptr += 1
}

function is_alphanum(text) {
    return /^[a-zA-Z0-9]+$/.test(text)
}
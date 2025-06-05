class PianoDisplay {
    constructor(display) {
        this.display = display

        this.line_height = 16
        this.font_size = 14
        this.max_visible_lines = Math.floor(this.display.height / this.line_height)
    }

    render(ctx) {
        ctx.fillStyle = this.display.color
        ctx.fillRect(this.display.offset_x, this.display.offset_y, this.display.width, this.display.height)
        ctx.font = `${this.font_size}px monospace`;
        ctx.fillStyle = "#AA2233"

        // console.log(this.error_stack)

        let h_step = this.display.height / this.max_visible_lines
        ERROR_STACK.forEach((error, i) => {
            ctx.fillText(error, this.display.offset_x + 10, this.display.offset_y + (i + 1) * h_step - h_step / 4);
        });
    }

}
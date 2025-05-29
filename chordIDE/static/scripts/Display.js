class Display {
    constructor(width, height, offset_x, offset_y, color) {
        this.width = width
        this.height = height
        this.offset_x = offset_x
        this.offset_y = offset_y
        this.color = color ? color : `#${Math.floor(Math.random() * 16777215).toString(16)}`
    }

    in_bounds(x, y) {
        // console.log(x, y, this.offset_x, this.offset_y)
        if (this.offset_x <= x && this.offset_x + this.width >= x) {
            if (this.offset_y <= y && this.offset_y + this.height >= y) {
                return true
            }
        }
        return false
    }

    render(ctx) {
        ctx.fillStyle = this.color
        ctx.fillRect(this.offset_x, this.offset_y, this.width, this.height)
    }
}
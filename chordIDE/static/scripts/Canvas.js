class Canvas {
    constructor(canvas){
        this.canvas = canvas
        this.ctx = canvas.getContext("2d")
        this.expected_size = new WeakMap()

        this.init()
    }

    init(){
        let rect = this.canvas.parentElement.getBoundingClientRect()
        this.canvas.width = rect.width
        this.canvas.height = rect.height

        console.log(this.canvas.parentElement, )
    }

    render(){
        this.ctx.fillStyle = "blue"
        this.ctx.fillRect(10,10,100,100)
    }
}
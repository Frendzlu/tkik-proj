class NoteDisplay {
    constructor(display) {
        this.display = display
        this.img = new Image()

        this.chord_code = "|  8  <4:4>  N.C.  Gm7/D  %  %  %  _  Gm7/D  _  |"
        handle_note_display(this, this.chord_code)
    }

    render(ctx) {
        ctx.fillStyle = this.display.color
        ctx.fillRect(this.display.offset_x, this.display.offset_y, this.display.width, this.display.height)

        ctx.drawImage(this.img, 0, 0, this.display.width, this.display.height, 0, 0, this.display.width, this.display.height)
    }
}

function handle_note_display(note_display) {
    let display = note_display.display
    let output = document.getElementById("output")
    output.height = display.height
    output.width = display.width

    let interval = setInterval(() => {
        draw_notes(display, note_display.chord_code)
        note_display.img.src = output.toDataURL()
        // console.log("śmiga", note_display)
    }, 200)
}

function draw_notes(display, chord_code) {
    const { Factory, EasyScore, System } = VexFlow
    const factory = new Factory({
        renderer: {
            elementId: "output",
            width: display.width,
            height: display.height,
        },
    })
    const score = factory.EasyScore()
    const system = factory.System()

    // let measures = chord_code.trim().split("|").filter(e => e != "").map(e => e.trim())
    // console.log(measures)

    system
        .addStave({
            voices: [
                score.voice(score.notes("C#5/q, B4, A4, G#4", { stem: "up" })),
                score.voice(score.notes("C#4/h, C#4", { stem: "down" })),
            ],
        })
        .addClef("treble")
        .addTimeSignature("4/4")

    factory.draw()
}
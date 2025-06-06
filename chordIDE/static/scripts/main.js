let canvasHTML = document.getElementById("root")
let canvas = new Canvas(canvasHTML)
const MOUSE = {
    x: 0,
    y: 0
}
const EVENTS = []
let ERROR_STACK = []
record_events()

canvas.set_size(window.innerWidth, window.innerHeight)
// handle_resize(canvas.canvasHTML)

let piano_separator_display = new Display(canvas.canvasHTML.width, 5, 0, canvas.canvasHTML.height * 0.75)
let note_display = new Display(canvas.canvasHTML.width / 2, canvas.canvasHTML.height * 0.75, 0, 0, "#DFD0B8")
let chord_code_display = new Display(canvas.canvasHTML.width / 2, canvas.canvasHTML.height * 0.75, canvas.canvasHTML.width / 2, 0, "#5a3f31")
let piano_display = new Display(canvas.canvasHTML.width, canvas.canvasHTML.height * 0.25, 0, canvas.canvasHTML.height * 0.75, "#222831")

//piano display will be... an error display for now : )
canvas.add_display(piano_separator_display)
// canvas.add_display(piano_display)
// canvas.add_display(note_display)
// canvas.add_display(chord_code_display)

let cc_display = new ChordCodeDisplay(chord_code_display, 30)
let cc_display_event_map = new Map([["mousedown", [set_focused_line]], ["keydown", [input_text]]])
let cc_display_UI = new UI(cc_display, ["mousedown", "keydown"], cc_display_event_map, [])
canvas.add_UI_element(cc_display_UI)

let nt_display = new NoteDisplay(note_display)
let nt_display_event_map = new Map([[]])
let nt_display_UI = new UI(nt_display, [], nt_display_event_map, [])
canvas.add_UI_element(nt_display_UI)

let err_display = new PianoDisplay(piano_display)
let err_display_event_map = new Map([[]])
let err_display_UI = new UI(err_display, [], err_display_event_map, [])
canvas.add_UI_element(err_display_UI)

let dragbar_display = new Display(7, note_display.height, canvas.canvasHTML.width / 2, 0, "black")
let dragbar_event_map = new Map([["mousedown", [handle_dragbar]], ["mouseup", [handle_dragbar]]])
let dragbar = new UI(dragbar_display, ["mousedown", "mouseup"], dragbar_event_map, [note_display, chord_code_display])
canvas.add_UI_element(dragbar)

canvas.render()
// window.alert("hello mr sigma, to compile your code you need to press '='")
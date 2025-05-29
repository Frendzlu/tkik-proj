class EventRecord {
    constructor(mouse, type, e) {
        this.x = mouse.x
        this.y = mouse.y
        this.type = type
        this.e = e
    }
}

function record_events() {
    window.addEventListener("mousemove", (e) => {
        MOUSE.x = e.clientX
        MOUSE.y = e.clientY

        EVENTS.push(new EventRecord(MOUSE, "mousemove"))
    })

    window.addEventListener("mousedown", (e) => {
        EVENTS.push(new EventRecord(MOUSE, "mousedown"))
    })

    window.addEventListener("mouseup", (e) => {
        EVENTS.push(new EventRecord(MOUSE, "mouseup"))
    })

    window.addEventListener("keydown", (e) => {
        EVENTS.push(new EventRecord(MOUSE, "keydown", e))
    })
}

//  on_mouse_down() {

//     }

//     on_mouse_up() {

//     }

//     on_drag() {

//     }

//     on_hover() {

//     }
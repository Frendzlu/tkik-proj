class Canvas {
    constructor(canvas) {
        this.canvasHTML = canvas
        this.ctx = canvas.getContext("2d")
        this.displays = []
        this.UI_elements = []
    }

    set_size(width, height) {
        this.canvasHTML.width = width
        this.canvasHTML.height = height
    }

    add_display(display) {
        this.displays.push(display)
    }

    add_UI_element(UI_elem) {
        this.UI_elements.push(UI_elem)
    }

    render_UI_elements() {
        for (const UI_elem of this.UI_elements) {
            UI_elem.render(this.ctx)
        }
    }

    handle_events() {
        while (EVENTS.length > 0) {
            let ev = EVENTS.shift()

            // console.log(ev)
            for (let i = 0; i < this.UI_elements.length; i++) {
                const elem = this.UI_elements[i]
                if (!elem.events.includes(ev.type)) continue
                if (!elem.display.in_bounds(MOUSE.x, MOUSE.y)) continue
                elem.dispatch_event(ev)
            }
        }
    }

    render() {
        for (const display of this.displays) {
            display.render(this.ctx)
        }

        this.handle_events()
        this.render_UI_elements()
        requestAnimationFrame(() => this.render())
    }
}

function handle_resize(canvas) {
    const observer = new ResizeObserver((entries) => {
        const entry = entries.find((entry) => entry.target === canvas)
        if (entry == null) return

        canvas.width = entry.devicePixelContentBoxSize[0].inlineSize
        canvas.height = entry.devicePixelContentBoxSize[0].blockSize
    })

    observer.observe(canvas)
}
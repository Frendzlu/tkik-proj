class UI {
    //connects displays with logic and user interaction
    constructor(display, events, event_to_fn_map, dependencies) {
        if (display.display != null) {
            this.display = display.display
            this.display_derivative = display
        }
        else {
            this.display = display
            this.display_derivative = null
        }
        this.events = events
        this.event_to_fn_map = event_to_fn_map
        this.dependencies = dependencies
        this.focused = false
    }

    dispatch_event(event) {
        let fns = this.event_to_fn_map.get(event.type)

        for (const fn of fns) {
            // console.log("skajbidi", this)
            fn(event, this)
        }
    }

    render(ctx) {
        if (this.display_derivative) this.display_derivative.render(ctx)
        else this.display.render(ctx)
    }
}

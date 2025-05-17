// dragbar - HTMLElement
// type    - "horizontal" or "vertical"
function handle_dragbar(dragbar, type) {
    const left_pane = dragbar.previousElementSibling
    const right_pane = dragbar.nextElementSibling
    const container = dragbar.parentElement

    let is_dragging = false
    dragbar.addEventListener("mousedown", (e) => {
        is_dragging = true
        if (type = "vertical") document.body.style.cursor = "col-resize"
        else document.body.style.cursor = "row-resize"
    })

    window.addEventListener("mousemove", (e) => {
        if (!is_dragging) return

        const container_rect = container.getBoundingClientRect()
        const offset = e.clientX - container_rect.left

        const percent_left = (offset / (container_rect.width - dragbar.clientWidth / 2)) * 100
        const percent_right = 100 - percent_left

        if (percent_left < 30 || percent_right < 30) return;
        left_pane.style.flex = `1 1 ${percent_left}%`
        right_pane.style.flex = `1 1 ${percent_right}%`

        console.log(getComputedStyle(left_pane).flex)
    })

    window.addEventListener("mouseup", (e) => {
        is_dragging = false
        document.body.style.cursor = "default"
    })
}
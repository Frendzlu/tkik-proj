function handle_resize(canvas) {
    const [display_width, display_height] = canvas.expected_size.get(canvas)
    const is_resized = canvas.width != display_width || canvas.height != display_height

    if (is_resized) {
        canvas.width = display_width
        canvas.height = display_height
    }

    return is_resized
}


function make_resize_observer(canvas){
    let resize_observer = new ResizeObserver((entries) => {
        requestAnimationFrame(() => {
            for (const entry of entries){
                let width;
                let height;
                let dpr = window.devicePixelRatio;
                if (entry.devicePixelContentBoxSize) {
                    width = entry.devicePixelContentBoxSize[0].inlineSize;
                    height = entry.devicePixelContentBoxSize[0].blockSize;
                    dpr = 1; // it's already in width and height
                } 
                else if (entry.contentBoxSize) {
                    if (entry.contentBoxSize[0]) {
                        width = entry.contentBoxSize[0].inlineSize;
                        height = entry.contentBoxSize[0].blockSize;
                    } 
                    else {
                        width = entry.contentBoxSize.inlineSize;
                        height = entry.contentBoxSize.blockSize;
                    }
                } 
                else {
                    width = entry.contentRect.width;
                    height = entry.contentRect.height;
                }

                // const expected_size = canvas.expected_size.get(entry.target)
                // if (entry.contentBoxSize[0].inlineSize === expected_size) {
                //     continue;
                // }
                const displayWidth = Math.round(width * dpr);
                const displayHeight = Math.round(height * dpr);

                const new_size = [displayWidth, displayHeight]
                canvas.expected_size.set(entry.target, new_size); 
            }
        })
    })

    resize_observer.observe(canvas.canvas)
}




















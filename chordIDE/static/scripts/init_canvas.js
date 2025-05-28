function init_canvas(canvas){
    cv = new Canvas(canvas)
    make_resize_observer(cv)
    return cv
}

function letter(target, control){
    return control.split(target).length - 1;
}

function solution(n, control) {
    
    n = n + letter("w", control);
    n = n - letter("s", control);
    n = n + letter("d", control) * 10;
    n = n - letter("a", control) * 10;
    
    return n;
}
/**
 * Site: stickers
 * Sticker Gallery
 */
document.getElementById('gallery_stickers').onclick = function(event) {
    event = event || window.event;
    var target = event.target || event.srcElement,
        link = target.src ? target.parentNode : target,
        options = {
            index: link,
            event: event,
            fullScreen: false,
            stretchImages: true
        },
        links = this.getElementsByTagName('a');
    blueimp.Gallery(links, options);
};

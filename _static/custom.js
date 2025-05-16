window.iFrameResizer = {
    onMessage(message) {
        if (message.type === 'remove' && Array.isArray(message.selectors)) {
            message.selectors.forEach(sel =>
                document.querySelectorAll(sel).forEach(el => el.remove())
            );
        }
    }
};


function wireDuplicateSidebarToggles() {
    for (const selector of [".primary-toggle", ".secondary-toggle"]) {
        const [controller, ...duplicates] = document.querySelectorAll(selector);

        for (const button of duplicates) {
            button.addEventListener("click", (event) => {
                event.preventDefault();
                event.stopPropagation();
                controller.click();
            });
        }
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wireDuplicateSidebarToggles);
} else {
    wireDuplicateSidebarToggles();
}
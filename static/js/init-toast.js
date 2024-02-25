$('.toast').each(function (index, element) {
    const toast = new bootstrap.Toast(element);
    toast.show();
});

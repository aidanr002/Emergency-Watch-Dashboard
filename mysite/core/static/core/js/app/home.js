function confirmDelete (id)
{
    cont = confirm("Are you sure want to delete this project?")
    if (cont)
    {
        url = "/delete-project/" + id;
        window.location = url;
    }
}

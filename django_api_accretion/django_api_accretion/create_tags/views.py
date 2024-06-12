from django.http import HttpResponse
from django.views import View
from database_visualization.views import GetPropertyDataImageLinkView

class CreateTagsView(View):
    def get(self, request):
        propertyID = request.GET.get('propertyid', '')
        address1 = request.GET.get('address1', '')
        address2 = request.GET.get('address2', '')

        data_view = GetPropertyDataImageLinkView()
        data = data_view.get_property_data(propertyID, address1, address2, request)

        if not data:
            return HttpResponse('<h1>Data not found</h1>', status=404)

        imageLink = data.get('imageLink', '')
        address_display = f"{address1}, {address2}"
        redirect_url = f"https://www.accretion.life/database/demo/view/?address1={address1}&address2={address2}"        
        tag_description = f"Check out the title history of {address_display}, with the best database visualization from Accretion."
        tag_title = "Accretion is building the best database for real estate titles.\n" + tag_description

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{tag_title}</title>
            <meta name="description" content="{tag_description}">
            
            <!-- Open Graph -->
            <meta property="og:type" content="website">
            <meta property="og:title" content="{tag_title}">
            <meta property="og:description" content="{tag_description}">
            <meta property="og:image:alt" content="{tag_description}">
            <meta property="og:image" content="{imageLink}">
            <meta property="og:url" content="{redirect_url}">
            <meta property="og:site_name" content="Accretion Database">
            <meta property="og:locale" content="en_US">
            
             <!-- Twitter -->
            <meta property="twitter:card" content="summary_large_image">
            <meta property="twitter:url" content="{redirect_url}">
            <meta property="twitter:site:id" content="@AccretionHome">
            <meta property="twitter:title" content="{tag_title}">
            <meta property="twitter:description" content="{tag_description}">
            <meta property="twitter:image" content="{imageLink}">
        </head>
        <body>
            <p>Meta tags have been generated for {address_display}</p>
            <p>{tag_title}</p>
            <img src={imageLink} />
        </body>
        </html>
        """

        return HttpResponse(html_content, content_type='text/html')

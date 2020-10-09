from django.views.generic import TemplateView
from . import models

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class contactPageView(TemplateView):
    template_name = 'contact_us.html'

class aboutPageView(TemplateView):
     template_name = 'about.html'

class cartPageView(TemplateView ):
    template_name = 'cart.html'

class cartemptyPageView(TemplateView ):
        template_name = 'cart_empty.html'

class faqPageView(TemplateView ):
        template_name = 'faq.html'

class logincustomerPageView(TemplateView ):
        template_name = 'login_customer.html'

class ordersreturnPageView(TemplateView ):
        template_name = 'orders_return.html'

class customerpasswordchangePageView(TemplateView):
        template_name = 'customer_password_change.html'

class customerpasswordforgotPageView(TemplateView):
        template_name = 'customer_password_forgot.html'

class customerprofilePageView(TemplateView):
        template_name = 'customer_profile.html'

class customerregisterPageView(TemplateView):
        template_name = 'customer_register.html'

class customerwelcomePageView(TemplateView):
        template_name = 'customer_welcome.html'

class logincustomerPageView(TemplateView):
        template_name = 'login_customer.html'

class privacyPageView(TemplateView):
        template_name = 'privacy.html'

class profileaddressesPageView(TemplateView):
        template_name = 'profile_addresses.html'

class profileadditionalinfoPageView(TemplateView):
        template_name = 'profile_additional_info.html'

class profilefavoritesPageView(TemplateView):
        template_name = 'profile_favorites.html'

class profileorderPageView(TemplateView):
        template_name = 'profile_order.html'

class profileorder2PageView(TemplateView):
        template_name = 'profile_order2.html'

class  profilepersonalinfoPageView(TemplateView):
        template_name = 'profile_personal_info.html'

class profileuserhistoryPageView(TemplateView):
        template_name = 'profile_user_history.html'

class searchPageView(TemplateView):
        template_name = 'search.html'

class shippingPageView(TemplateView):
        template_name = 'shipping.html'

class shippingcomplatebuyPageView(TemplateView):
        template_name = 'shipping_complate_buy.html'

class shippingnocomplatebuyPageView(TemplateView):
        template_name = 'shipping_no_complate_buy.html'

class shippingpaymentPageView(TemplateView):
        template_name = 'shipping_payment.html'

class singlenoproductPageView(TemplateView):
      template_name = 'single_no_product.html'

class singleproductPageView(TemplateView):
        template_name = 'single_product.html'

class verifyphonenumberPageView(TemplateView):
        template_name = 'verify_phone_number.html'

class productcommentPageView(TemplateView):
        template_name = 'product_comment.html'

class Error404pageView(TemplateView ):
        template_name = '404.html'




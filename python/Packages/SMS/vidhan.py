# SMS ---> vidhan file or module

# first method start for whole package

# import Admin.service
# Admin.service.admin_service()

# import Admin.product
# Admin.product.admin_product()

# import Admin.Common.footer
# Admin.Common.footer.admin_common_footer()

# import Tech.profile
# Tech.profile.tech_profile()

# first method end

# second method start for whole module

# from Admin import service
# service.admin_service()

# from Admin.Common import header
# header.admin_common_header()

# from User import reqst
# reqst.user_request()

# second method end

# third method start for particular fun or class or var

# from Admin.product import admin_product
# admin_product()

# from Admin.Common.footer import admin_common_footer
# admin_common_footer()

# look carefully start

# from Admin import product, service
# service.admin_service()
# product.admin_product()

# from Admin import *
# service.admin_service()
# product.admin_product()

# from Admin.Common import *
# header.admin_common_header()
# footer.admin_common_footer()

# look carefully end

# using work form tech with user request

from Tech import work
work.tech_work()

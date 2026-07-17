from rest_framework import routers
from staff.staffviewset import StaffViewSet
from authentication.viewsets.register import RegisterViewSet
from authentication.viewsets.login import LoginViewSet
from appointment.viewset import AppointmentViewset
from car.viewset import CarViewset
from user.viewset import CustomerViewset
from invoices.viewset import InvoiceViewSet
from quotation.viewset import QuotationViewSet
from workorder.viewset import WorkOrderViewSet
from service.viewset import ServiceViewSet

router = routers.SimpleRouter()

router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'register-staff', RegisterViewSet, basename='register-staff')
router.register(r'log-in', LoginViewSet, basename='log-in')
router.register(r'create-appointment', AppointmentViewset, basename='create-appointment')
router.register(r'add-car', CarViewset, basename='add-car')
router.register(r'add-customer', CustomerViewset, basename='add-customer')
router.register(r'create-invoice', InvoiceViewSet, basename='create-invoice')
router.register(r'create-quotation', QuotationViewSet, basename='create-quotation')
router.register(r'create-workorder', WorkOrderViewSet, basename='create-workorder')
router.register(r'create-service', ServiceViewSet, basename='create-service')

urlpatterns = [
    *router.urls,
]

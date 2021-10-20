from enum import Enum


class ReportType(str, Enum):
    GET_V2_SELLER_PERFORMANCE_REPORT = 'GET_V2_SELLER_PERFORMANCE_REPORT'
    GET_FLAT_FILE_OPEN_LISTINGS_DATA = 'GET_FLAT_FILE_OPEN_LISTINGS_DATA'
    GET_MERCHANT_LISTINGS_ALL_DATA = 'GET_MERCHANT_LISTINGS_ALL_DATA'
    GET_MERCHANT_LISTINGS_DATA = 'GET_MERCHANT_LISTINGS_DATA'
    GET_MERCHANT_LISTINGS_INACTIVE_DATA = 'GET_MERCHANT_LISTINGS_INACTIVE_DATA'
    GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT = 'GET_MERCHANT_LISTINGS_DATA_BACK_COMPAT'
    GET_MERCHANT_LISTINGS_DATA_LITE = 'GET_MERCHANT_LISTINGS_DATA_LITE'
    GET_MERCHANT_LISTINGS_DATA_LITER = 'GET_MERCHANT_LISTINGS_DATA_LITER'
    GET_MERCHANT_CANCELLED_LISTINGS_DATA = 'GET_MERCHANT_CANCELLED_LISTINGS_DATA'
    GET_MERCHANT_LISTINGS_DEFECT_DATA = 'GET_MERCHANT_LISTINGS_DEFECT_DATA'
    GET_PAN_EU_OFFER_STATUS = 'GET_PAN_EU_OFFER_STATUS'
    GET_MFN_PAN_EU_OFFER_STATUS = 'GET_MFN_PAN_EU_OFFER_STATUS'
    GET_FLAT_FILE_GEO_OPPORTUNITIES = 'GET_FLAT_FILE_GEO_OPPORTUNITIES'
    GET_REFERRAL_FEE_PREVIEW_REPORT = 'GET_REFERRAL_FEE_PREVIEW_REPORT'
    GET_FLAT_FILE_ACTIONABLE_ORDER_DATA_SHIPPING = 'GET_FLAT_FILE_ACTIONABLE_ORDER_DATA_SHIPPING'
    GET_ORDER_REPORT_DATA_INVOICING = 'GET_ORDER_REPORT_DATA_INVOICING'
    GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING = 'GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING'
    GET_ORDER_REPORT_DATA_TAX = 'GET_ORDER_REPORT_DATA_TAX'
    GET_FLAT_FILE_ORDER_REPORT_DATA_TAX = 'GET_FLAT_FILE_ORDER_REPORT_DATA_TAX'
    GET_ORDER_REPORT_DATA_SHIPPING = 'GET_ORDER_REPORT_DATA_SHIPPING'
    GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING = 'GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING'
    GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL = 'GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL'
    GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL = 'GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL'
    GET_FLAT_FILE_ARCHIVED_ORDERS_DATA_BY_ORDER_DATE = 'GET_FLAT_FILE_ARCHIVED_ORDERS_DATA_BY_ORDER_DATE'
    GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL = 'GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL'
    GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL = 'GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL'
    GET_FLAT_FILE_PENDING_ORDERS_DATA = 'GET_FLAT_FILE_PENDING_ORDERS_DATA'
    GET_PENDING_ORDERS_DATA = 'GET_PENDING_ORDERS_DATA'
    GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA = 'GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA'
    GET_XML_RETURNS_DATA_BY_RETURN_DATE = 'GET_XML_RETURNS_DATA_BY_RETURN_DATE'
    GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE = 'GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE'
    GET_XML_MFN_PRIME_RETURNS_REPORT = 'GET_XML_MFN_PRIME_RETURNS_REPORT'
    GET_CSV_MFN_PRIME_RETURNS_REPORT = 'GET_CSV_MFN_PRIME_RETURNS_REPORT'
    GET_XML_MFN_SKU_RETURN_ATTRIBUTES_REPORT = 'GET_XML_MFN_SKU_RETURN_ATTRIBUTES_REPORT'
    GET_FLAT_FILE_MFN_SKU_RETURN_ATTRIBUTES_REPORT = 'GET_FLAT_FILE_MFN_SKU_RETURN_ATTRIBUTES_REPORT'
    GET_SELLER_FEEDBACK_DATA = 'GET_SELLER_FEEDBACK_DATA'
    GET_V1_SELLER_PERFORMANCE_REPORT = 'GET_V1_SELLER_PERFORMANCE_REPORT'
    GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE = 'GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE'
    GET_V2_SETTLEMENT_REPORT_DATA_XML = 'GET_V2_SETTLEMENT_REPORT_DATA_XML'
    GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2 = 'GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2'
    GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL = 'GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL'
    GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING = 'GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING'
    GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX = 'GET_AMAZON_FULFILLED_SHIPMENTS_DATA_TAX'
    GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA = 'GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA'
    GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA = 'GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA'
    GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA = 'GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA'
    GET_REMOTE_FULFILLMENT_ELIGIBILITY = 'GET_REMOTE_FULFILLMENT_ELIGIBILITY'
    GET_AFN_INVENTORY_DATA = 'GET_AFN_INVENTORY_DATA'
    GET_AFN_INVENTORY_DATA_BY_COUNTRY = 'GET_AFN_INVENTORY_DATA_BY_COUNTRY'
    GET_LEDGER_SUMMARY_VIEW_DATA = 'GET_LEDGER_SUMMARY_VIEW_DATA'
    GET_LEDGER_DETAIL_VIEW_DATA = 'GET_LEDGER_DETAIL_VIEW_DATA'
    GET_FBA_FULFILLMENT_CURRENT_INVENTORY_DATA = 'GET_FBA_FULFILLMENT_CURRENT_INVENTORY_DATA'
    GET_FBA_FULFILLMENT_MONTHLY_INVENTORY_DATA = 'GET_FBA_FULFILLMENT_MONTHLY_INVENTORY_DATA'
    GET_FBA_FULFILLMENT_INVENTORY_RECEIPTS_DATA = 'GET_FBA_FULFILLMENT_INVENTORY_RECEIPTS_DATA'
    GET_RESERVED_INVENTORY_DATA = 'GET_RESERVED_INVENTORY_DATA'
    GET_FBA_FULFILLMENT_INVENTORY_SUMMARY_DATA = 'GET_FBA_FULFILLMENT_INVENTORY_SUMMARY_DATA'
    GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA = 'GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA'
    GET_FBA_FULFILLMENT_INVENTORY_HEALTH_DATA = 'GET_FBA_FULFILLMENT_INVENTORY_HEALTH_DATA'
    GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA = 'GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA'
    GET_FBA_MYI_ALL_INVENTORY_DATA = 'GET_FBA_MYI_ALL_INVENTORY_DATA'
    GET_RESTOCK_INVENTORY_RECOMMENDATIONS_REPORT = 'GET_RESTOCK_INVENTORY_RECOMMENDATIONS_REPORT'
    GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA = 'GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA'
    GET_STRANDED_INVENTORY_UI_DATA = 'GET_STRANDED_INVENTORY_UI_DATA'
    GET_STRANDED_INVENTORY_LOADER_DATA = 'GET_STRANDED_INVENTORY_LOADER_DATA'
    POST_FLAT_FILE_INVLOADER_DATA = 'POST_FLAT_FILE_INVLOADER_DATA'
    GET_FBA_INVENTORY_AGED_DATA = 'GET_FBA_INVENTORY_AGED_DATA'
    GET_EXCESS_INVENTORY_DATA = 'GET_EXCESS_INVENTORY_DATA'
    GET_FBA_STORAGE_FEE_CHARGES_DATA = 'GET_FBA_STORAGE_FEE_CHARGES_DATA'
    GET_PRODUCT_EXCHANGE_DATA = 'GET_PRODUCT_EXCHANGE_DATA'
    GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA = 'GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA'
    GET_FBA_REIMBURSEMENTS_DATA = 'GET_FBA_REIMBURSEMENTS_DATA'
    GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA = 'GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA'
    GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA = 'GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA'
    GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA = 'GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA'
    GET_FBA_RECOMMENDED_REMOVAL_DATA = 'GET_FBA_RECOMMENDED_REMOVAL_DATA'
    GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA = 'GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA'
    GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA = 'GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA'
    GET_FBA_UNO_INVENTORY_DATA = 'GET_FBA_UNO_INVENTORY_DATA'
    GET_FLAT_FILE_SALES_TAX_DATA = 'GET_FLAT_FILE_SALES_TAX_DATA'
    SC_VAT_TAX_REPORT = 'SC_VAT_TAX_REPORT'
    GET_VAT_TRANSACTION_DATA = 'GET_VAT_TRANSACTION_DATA'
    GET_GST_MTR_B2B_CUSTOM = 'GET_GST_MTR_B2B_CUSTOM'
    GET_GST_MTR_B2C_CUSTOM = 'GET_GST_MTR_B2C_CUSTOM'
    GET_XML_BROWSE_TREE_DATA = 'GET_XML_BROWSE_TREE_DATA'
    GET_EASYSHIP_DOCUMENTS = 'GET_EASYSHIP_DOCUMENTS'
    GET_EASYSHIP_PICKEDUP = 'GET_EASYSHIP_PICKEDUP'
    GET_EASYSHIP_WAITING_FOR_PICKUP = 'GET_EASYSHIP_WAITING_FOR_PICKUP'
    RFQD_BULK_DOWNLOAD = 'RFQD_BULK_DOWNLOAD'
    FEE_DISCOUNTS_REPORT = 'FEE_DISCOUNTS_REPORT'
    GET_FLAT_FILE_OFFAMAZONPAYMENTS_SANDBOX_SETTLEMENT_DATA = 'GET_FLAT_FILE_OFFAMAZONPAYMENTS_SANDBOX_SETTLEMENT_DATA'
    GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT = 'GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT'
    GET_VENDOR_SALES_DIAGNOSTIC_REPORT = 'GET_VENDOR_SALES_DIAGNOSTIC_REPORT'
    GET_VENDOR_INVENTORY_HEALTH_AND_PLANNING_REPORT = 'GET_VENDOR_INVENTORY_HEALTH_AND_PLANNING_REPORT'
    GET_VENDOR_DEMAND_FORECAST_REPORT = 'GET_VENDOR_DEMAND_FORECAST_REPORT'

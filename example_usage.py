from client import MultiCloudDigitalTransformationCartridgeClient

def main():
    client = MultiCloudDigitalTransformationCartridgeClient()
    res = client.integrate_multicloud_commerce_cartridge('Haute_Horlogerie_Swiss_Group')
    print('Audit: ' + res['integration_audit_id'] + ' for ' + res['brand_ecosystem'])
    print('Time to Market: ' + str(res['cartridge_time_to_market_weeks']) + ' wks vs Legacy: ' + str(res['legacy_turnaround_time_weeks']) + ' wks')
    print('Cloud Pillars: ' + ', '.join(res['integrated_cloud_pillars']) + ' (Unified POS: ' + str(res['omnichannel_pos_order_routing_unified']) + ')')

if __name__ == '__main__':
    main()

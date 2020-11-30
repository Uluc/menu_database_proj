import os, sys,time
dir_path = str(os.path.dirname(os.path.realpath(__file__)))
dir_path = dir_path[:-16]
sys.path.insert(0, dir_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'PET.settings'
from django.conf import settings
import django
django.setup()

from projects.models import Project, RelaySetting, Site, DrawingTime, GeoTech
from resources.models import Resource, RateSheet
from drawings.models import WBSCode, Drawing

global project
if not Project.objects.filter(name="Entergy Default").exists():
    project = Project(name="Entergy Default")
    project.save()
    site = Site(name="Default Site", project=project)
    site.save()

else:
    site = Site.objects.get(name="Default Site")
    project = site.project

WBSCode.objects.all().delete()
Drawing.objects.all().delete()

def add_wbs_codes(code_dict):
    for code in code_dict:
        if not WBSCode.objects.filter(code=code["code"],description=code['description'],category=code['category'],activity_type=code['type']).exists():
            new_code = WBSCode(code=code["code"],description=code['description'],category=code['category'],activity_type=code['type'])
            new_code.save()


def add_relay_drawings(drawing_dict):
    Drawing.objects.all().delete()
    for drawing in drawing_dict:
        if len(WBSCode.objects.filter(code=drawing["code"])) > 1:
            print(WBSCode.objects.filter(code=drawing["code"]))
        if not Drawing.objects.filter(activity_type="relay",
                                      size=drawing['size'],
                                      code=WBSCode.objects.get(code=drawing["code"]),
                                      description=drawing['description'],
                                      category=drawing['category'],
                                      drawings_each=drawing['dwg_each'],
                                      site = site).exists():
            new_drawing = Drawing(activity_type="relay",
                                  size=drawing['size'],
                                  code=WBSCode.objects.get(code=drawing["code"]),
                                  description=drawing['description'],
                                  category=drawing['category'],
                                  drawings_each=drawing['dwg_each'],
                                  site = site)
            new_drawing.save()



def add_substation_drawings(drawing_dict):
    for drawing in drawing_dict:
        if len(WBSCode.objects.filter(code=drawing["code"])) > 1:
            print(WBSCode.objects.filter(code=drawing["code"]))
        if not Drawing.objects.filter(activity_type="substation",
                                      size=drawing['size'],
                                      code=WBSCode.objects.get(code=drawing["code"]),
                                      description=drawing['description'],
                                      category=drawing['category'],
                                      drawings_each=drawing['dwg_each'],
                                      site = site).exists():
            new_drawing = Drawing(activity_type="substation",
                                  size=drawing['size'],
                                  code=WBSCode.objects.get(code=drawing["code"]),
                                  description=drawing['description'],
                                  category=drawing['category'],
                                  drawings_each=drawing['dwg_each'],
                                  site = site)
            new_drawing.save()

def add_resources(resource_dict):
    Resource.objects.all().delete()
    for key,val in resource_dict.items():
        if not RateSheet.objects.filter(name=key).exists():
            rate_sheet = RateSheet(name=key)
            rate_sheet.save()
        else:
            rate_sheet = RateSheet.objects.get(name=key)
        for resource in val:
            if not Resource.objects.filter(classification=resource["classification"],rate=resource['rate'], rate_sheet=rate_sheet).exists():
                new_resource = Resource(classification=resource["classification"],rate=resource['rate'], rate_sheet=rate_sheet)
                new_resource.save()

def add_relay_settings(relay_setting_dict):
    RelaySetting.objects.all().delete()
    for setting in relay_setting_dict:
        if not RelaySetting.objects.filter(description=setting["description"], cost_per_relay=setting["cost_per_relay"], hours_per_device=setting["hours_per_device"], category=setting['category'],site = site).exists():
            new_setting = RelaySetting(description=setting["description"], cost_per_relay=setting["cost_per_relay"], hours_per_device=setting["hours_per_device"], category=setting['category'],site = site)
            new_setting.save()

def add_geo_tech(geo_tech_dict):
    GeoTech.objects.all().delete()
    for tech in geo_tech_dict:
        if not GeoTech.objects.filter(description=tech['description'], rate=tech['cost_per_geo_tech'], category='Site', activity_type='substation', site=site).exists():
            new_geo_tech = GeoTech(description=tech['description'], rate=tech['cost_per_geo_tech'], category='Site', activity_type='substation', site=site)
            new_geo_tech.save()
            print(new_geo_tech.description)

def add_drawing_time(drawing_times):
    DrawingTime.objects.all().delete()
    # if not project.relay_drawing_time.exists():
    relay_drawing_time = DrawingTime(activity_type=drawing_times[1]["activity_type"],
                                     engineer_new_drawing=drawing_times[1]["engineer_new_drawing"], engineer_retro_drawing=drawing_times[1]["engineer_retro_drawing"],
                                     designer_new_drawing=drawing_times[1]["designer_new_drawing"], designer_retro_drawing=drawing_times[1]["designer_retro_drawing"],
                                     drafter_new_drawing=drawing_times[1]["drafter_new_drawing"], drafter_retro_drawing=drawing_times[1]["drafter_retro_drawing"],
                                     a=drawing_times[1]["a"], b=drawing_times[1]["b"], c=drawing_times[1]["c"], d=drawing_times[1]["d"], e=drawing_times[1]["e"],)
    relay_drawing_time.save()
    project.relay_drawing_time = relay_drawing_time


    # if not project.substation_drawing_time:
    electrical_drawing_time = DrawingTime(activity_type=drawing_times[0]["activity_type"],
                                          engineer_new_drawing=drawing_times[0]["engineer_new_drawing"], engineer_retro_drawing=drawing_times[0]["engineer_retro_drawing"],
                                          designer_new_drawing=drawing_times[0]["designer_new_drawing"], designer_retro_drawing=drawing_times[0]["designer_retro_drawing"],
                                          drafter_new_drawing=drawing_times[0]["drafter_new_drawing"], drafter_retro_drawing=drawing_times[0]["drafter_retro_drawing"],
                                          a=drawing_times[0]["a"], b=drawing_times[0]["b"], c=drawing_times[0]["c"], d=drawing_times[0]["d"], e=drawing_times[0]["e"],)
    electrical_drawing_time.save()
    project.electrical_drawing_time = electrical_drawing_time

    site_drawing_time = DrawingTime(activity_type=drawing_times[0]["activity_type"],
                                          engineer_new_drawing=drawing_times[0]["engineer_new_drawing"], engineer_retro_drawing=drawing_times[0]["engineer_retro_drawing"],
                                          designer_new_drawing=drawing_times[0]["designer_new_drawing"], designer_retro_drawing=drawing_times[0]["designer_retro_drawing"],
                                          drafter_new_drawing=drawing_times[0]["drafter_new_drawing"], drafter_retro_drawing=drawing_times[0]["drafter_retro_drawing"],
                                          a=drawing_times[0]["a"], b=drawing_times[0]["b"], c=drawing_times[0]["c"], d=drawing_times[0]["d"], e=drawing_times[0]["e"],)
    site_drawing_time.save()
    project.electrical_drawing_time = site_drawing_time

    foundation_drawing_time = DrawingTime(activity_type=drawing_times[0]["activity_type"],
                                          engineer_new_drawing=drawing_times[0]["engineer_new_drawing"], engineer_retro_drawing=drawing_times[0]["engineer_retro_drawing"],
                                          designer_new_drawing=drawing_times[0]["designer_new_drawing"], designer_retro_drawing=drawing_times[0]["designer_retro_drawing"],
                                          drafter_new_drawing=drawing_times[0]["drafter_new_drawing"], drafter_retro_drawing=drawing_times[0]["drafter_retro_drawing"],
                                          a=drawing_times[0]["a"], b=drawing_times[0]["b"], c=drawing_times[0]["c"], d=drawing_times[0]["d"], e=drawing_times[0]["e"],)
    foundation_drawing_time.save()
    project.electrical_drawing_time = foundation_drawing_time
    project.save()


wbs_codes = [
    # substation wbs codes
    {'code': '11010', 'description': 'Scope, Budget, Schedules & Drawings', 'category': 'Overhead/Scoping', 'type': 'substation'},
    {'code': '11210', 'description': 'Site Drawings & Calculations', 'category': 'Civil & Site', 'type': 'substation'},
    {'code': '11250', 'description': 'Storm Water Plan (SWPPP)', 'category': 'Civil & Site', 'type': 'substation'},
    {'code': '11310', 'description': 'Foundation Plan, Details & Calculations', 'category': 'Foundation & Structural', 'type': 'substation'},
    {'code': '11330', 'description': 'Structural Drawings & Calculations (Vendor RVW)', 'category': 'Foundation & Structural', 'type': 'substation'},
    {'code': '11410', 'description': "Electrical & Shielding Plan, Details & Calc's", 'category': 'Electrical', 'type': 'substation'},
    {'code': '11430', 'description': 'Grounding, Conduit, Lighting Plan & Details', 'category': 'Electrical', 'type': 'substation'},
    {'code': '11470', 'description': 'Control House (Layout, Wall Elevations, etc.)', 'category': 'Electrical', 'type': 'substation'},
    {'code': '11510', 'description': 'Study Support', 'category': 'Studies & Specs', 'type': 'substation'},
    {'code': '11520', 'description': 'Equipment & Constructions Specifications', 'category': 'Studies & Specs', 'type': 'substation'},
    {'code': '11610', 'description': 'Lead Design Engineer Touches', 'category': 'Design Costs', 'type': 'substation'},
    {'code': '11620', 'description': 'QA/QC', 'category': 'Design Costs', 'type': 'substation'},
    {'code': '11660', 'description': 'Meetings, Site Visits & Field Trips', 'category': 'Design Costs', 'type': 'substation'},
    {'code': '11680', 'description': 'As Built', 'category': 'Design Costs', 'type': 'substation'},
    {'code': '11690', 'description': 'Project Closeout', 'category': 'Design Costs', 'type': 'substation'},
    {'code': '11710', 'description': 'Procurement Support', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11720', 'description': 'PM/PE Support', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11730', 'description': 'Construction Support', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11740', 'description': 'Principal Eng and Design Managere Support', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11750', 'description': 'Project Manager - Project Activities', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11760', 'description': 'Admin Support', 'category': 'Project Support', 'type': 'substation'},
    {'code': '11810', 'description': 'Change Management (Risk)', 'category': 'Change Management', 'type': 'substation'},
    {'code': '11860', 'description': 'Computer Issues', 'category': 'Change Management', 'type': 'substation'},
    {'code': '11910', 'description': 'Reproduction', 'category': 'Misc. Codes', 'type': 'substation'},
    {'code': '11920', 'description': 'Outside Services', 'category': 'Misc. Codes', 'type': 'substation'},
    {'code': '61000', 'description': 'Proposal Substation', 'category': 'Misc. Codes', 'type': 'substation'},

    # relay wbs codes
    {'code': '12010', 'description': 'Scoping Activities', 'category': 'Contract Scoping', 'type': 'relay'},
    {'code': '12110', 'description': 'Scope, Budget, Schedule, Report & Plan', 'category': 'Project Preparation', 'type': 'relay'},
    {'code': '12120', 'description': 'Drawing List', 'category': 'Project Preparation', 'type': 'relay'},
    {'code': '12130', 'description': 'Relaying One-Line', 'category': 'Project Preparation', 'type': 'relay'},
    {'code': '12210', 'description': 'XFMR Diff Panels', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12220', 'description': 'Bus Diff Panels', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12230', 'description': 'Line/Breaker Panels', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12240', 'description': 'Line Panels', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12250', 'description': 'Breaker Control Panels', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12260', 'description': 'Mimic Bus', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12270', 'description': 'Meter Panel', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12280', 'description': 'Dist Brkr Protection (IPAC) Cabinets', 'category': 'Primary Panels', 'type': 'relay'},
    {'code': '12310', 'description': 'RTU Panels', 'category': 'Secondary Panels', 'type': 'relay'},
    {'code': '12320', 'description': 'Host Edit Sheet', 'category': 'Secondary Panels', 'type': 'relay'},
    {'code': '12330', 'description': 'DFR Panel', 'category': 'Seitem.category == "Panels"condary Panels', 'type': 'relay'},
    {'code': '12340', 'description': 'Comm Panel & Equipment', 'category': 'Secondary Panels', 'type': 'relay'},
    {'code': '12350', 'description': 'DTT Panel', 'category': 'Secondary Panels', 'type': 'relay'},
    {'code': '12410', 'description': 'Control House', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12420', 'description': 'Term CAB', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12430', 'description': 'Junction Boxes', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12440', 'description': 'Equipment CABs', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12450', 'description': 'Cable Pull List/Schedule development', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12460', 'description': 'AC/DC Cabinets', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12470', 'description': 'Bill of Materials', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12480', 'description': 'Custom Panels', 'category': 'Support Panels & Cabinets', 'type': 'relay'},
    {'code': '12510', 'description': 'Relay Settings', 'category': 'Studies, Calcs & Setting', 'type': 'relay'},
    {'code': '12520', 'description': 'Coordination Studies', 'category': 'Studies, Calcs & Setting', 'type': 'relay'},
    {'code': '12530', 'description': 'Voltage Drop', 'category': 'Studies, Calcs & Setting', 'type': 'relay'},
    {'code': '12540', 'description': 'AC/DC Load Calculations', 'category': 'Studies, Calcs & Setting', 'type': 'relay'},
    {'code': '12610', 'description': 'Lead Design Engineer Touches', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12620', 'description': 'QA/QC', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12630', 'description': 'Drafting Support', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12640', 'description': 'Modeling Support', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12650', 'description': 'Drawing Package Preparation (Blue Book, Reproduction)', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12660', 'description': 'Meetings', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12670', 'description': 'Site/Field Trips', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12680', 'description': 'AS-Built', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12690', 'description': 'Project Closeout', 'category': 'Design Costs', 'type': 'relay'},
    {'code': '12710', 'description': 'Procurement Support', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12720', 'description': 'PM/PE Support', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12730', 'description': 'Construction Support', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12740', 'description': 'Design Manager & Principal Engineer Support', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12750', 'description': 'Project Manager - Project Activities', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12760', 'description': 'Admin Support', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12770', 'description': 'PM Project Assist', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12780', 'description': 'Design Manager', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12790', 'description': 'Administration', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12791', 'description': 'Training', 'category': 'Project Support', 'type': 'relay'},
    {'code': '12810', 'description': 'Implement Risk Identified in a Proposal', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12820', 'description': 'Changes in Scope/Scope Creep', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12830', 'description': 'Estimate Problem', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12840', 'description': 'Procurement Problem', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12850', 'description': 'Design Info (lack of)', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12860', 'description': 'Computer Issues', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12870', 'description': 'Internal Change (Non-billable Hours to Customer)', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12880', 'description': 'Changes to Reduce Budget/Schedule', 'category': 'Change Management', 'type': 'relay'},
    {'code': '12890', 'description': 'Preference Requests, Engineering and Field', 'category': 'Change Management', 'type': 'relay'},
    {'code': '62000', 'description': 'Proposals Estimates, Bid Support & Issuing Bids', 'category': 'Project Estimation', 'type': 'relay'},
]


relay_drawings = [
    {'size': 'A', 'code': '12650', 'category': 'Miscellaneous',  'description': 'Purchase Recs', 'dwg_each': 1, 'qc_hrs': 0},
    {'size': 'E', 'code': '12120', 'category': 'Miscellaneous',  'description': 'Cover / Index', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12130', 'category': 'Miscellaneous',  'description': 'Operational Oneline', 'dwg_each': 1, 'qc_hrs': 1},
    {'size': 'E', 'code': '12130', 'category': 'Miscellaneous',  'description': 'Communication Oneline', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12130', 'category': 'Miscellaneous',  'description': 'Three Lines', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': '230kV Breaker Panels (30") PM0501 Opt B New (w/ MOS)', 'dwg_each': 11, 'qc_hrs': 6},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': '230kV IPO Breaker Panels (30") PM0501 Opt B New (w/o MOS)', 'dwg_each': 9, 'qc_hrs': 8},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': '230kV Breaker Panel, 30" (SEL-451-5) New', 'dwg_each': 	9, 'qc_hrs': 6},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': '500kV Breaker Panels (Mod)',	'dwg_each': 7, 'qc_hrs': 6},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': 'Dual Breaker Control Panel, 28" (Mod)', 'dwg_each': 12, 'qc_hrs': 7},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': 'Feeder Breaker Feeding XFMR Control (PM0501 Opt A SEL-351-7)', 'dwg_each': 9, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12270', 'category': 'Panels',  'description': 'Meter Panel 30" - Two Meters', 'dwg_each': 4, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': 'Xfmr / Breaker Panel', 'dwg_each': 11, 'qc_hrs': 7},
    {'size': 'E', 'code': '12230', 'category': 'Panels',  'description': 'Line / Breaker Panel PM1803 Opt B (New)', 'dwg_each': 9, 'qc_hrs': 8},
    {'size': 'E', 'code': '12230', 'category': 'Panels',  'description': 'Line Panel Removal', 'dwg_each': 3, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12250', 'category': 'Panels',  'description': 'Breaker Control Panel Removal', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': 'XFMR Diff Relay Panel Removal', 'dwg_each': 6, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12240', 'category': 'Panels',  'description': 'Line Panel (30") PM1803 Opt C2 (SEL-421/SEL-411L) New', 'dwg_each': 8, 'qc_hrs': 8},
    {'size': 'E', 'code': '12240', 'category': 'Panels',  'description': '138kV Line Panel (30") PM1803 Opt C (SEL-421/SEL-311C) New', 'dwg_each': 7, 'qc_hrs': 4},
    {'size': 'E', 'code': '12240', 'category': 'Panels',  'description': 'Lines Panels, 30" (Dual SEL-411L - Std PM1803 Opt C5 ) (New)', 'dwg_each': 9, 'qc_hrs': 8},
    {'size': 'E', 'code': '12240', 'category': 'Panels',  'description': 'Line Panel, 30" (Dual SEL-411L) (New)', 'dwg_each': 9, 'qc_hrs': 6},
    {'size': 'E', 'code': '12240', 'category': 'Panels',  'description': 'Line Relay Panel, 30" (SEL-421 & SEL-311C - Std PM1803 Option C) (Mod)', 'dwg_each': 6, 'qc_hrs': 6},
    {'size': 'E', 'code': '12220', 'category': 'Panels',  'description': '230kV Bus Differential Panel, 30" (PM0602-C w/o ARs) (New)',	'dwg_each': 5, 'qc_hrs': 9},
    {'size': 'E', 'code': '12220', 'category': 'Panels',  'description': 'Existing Bus Diff Panel Modifications', 'dwg_each': 5, 'qc_hrs': 3},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': '230kV XFMR Diff Relay Panel (30") Customed PM3505-C & PM3505-B New', 'dwg_each': 12, 'qc_hrs': 9},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': 'XFMR Diff Relay Panel (30") (PM3507-A) New', 'dwg_each': 10, 'qc_hrs': 7},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': 'XFMR Diff Relay Panel (30") (PM3507-E) New', 'dwg_each': 5, 'qc_hrs': 9},
    {'size': 'E', 'code': '12210', 'category': 'Panels',  'description': 'Lines Panels, 30" (Dual SEL-411L - Std PM1803 Opt C5 ) (New)(w/o MOS)', 'dwg_each': 8, 'qc_hrs': 6},
    {'size': 'E', 'code': '12220', 'category': 'Panels',  'description': 'Existing Bus Diff Drawings (Mod)', 'dwg_each': 8, 'qc_hrs': 1},
    {'size': 'E', 'code': '12480', 'category': 'Panels',  'description': 'MOS Cabinet', 'dwg_each': 3,	'qc_hrs': 0.5},
    {'size': 'A', 'code': '12320', 'category': 'Miscellaneous',  'description': 'RTU Points List', 'dwg_each': 3, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12310', 'category': 'RTU & Communication Panels',  'description': 'RTU - Supervisory Processor Panel 24" (New)', 'dwg_each': 8, 'qc_hrs': 4},
    {'size': 'E', 'code': '12310', 'category': 'RTU & Communication Panels',  'description': 'RTU Network Interface Panels 24" (Power)', 'dwg_each': 2, 'qc_hrs': 2},
    {'size': 'E', 'code': '12310', 'category': 'RTU & Communication Panels',  'description': 'RTU Dual Train Panel 24"', 'dwg_each': 2, 'qc_hrs': 2},
    {'size': 'E', 'code': '12310', 'category': 'RTU & Communication Panels',  'description': 'RTU 24" Peripheral Panel', 'dwg_each': 4, 'qc_hrs': 2},
    {'size': 'E', 'code': '12340', 'category': 'Connection Diagrams',  'description': 'Comm / Connect Diagram', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12340', 'category': 'RTU & Communication Panels',  'description': 'Communication 24" Panel (New)', 'dwg_each': 4, 'qc_hrs': 1},
    {'size': 'E', 'code': '12340', 'category': 'RTU & Communication Panels',  'description': 'Comm Panel - 230kV/115kV Annun. & Comm Processor', 'dwg_each': 3, 'qc_hrs': 1},
    {'size': 'E', 'code': '12340', 'category': 'RTU & Communication Panels',  'description': 'Annunciators', 'dwg_each': 3, 'qc_hrs': 1},
    {'size': 'E', 'code': '12340', 'category': 'RTU & Communication Panels',  'description': 'Trap & Tuner Removal', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12330', 'category': 'RTU & Communication Panels',  'description': 'DFR Panel', 'dwg_each': 4, 'qc_hrs': 2},
    {'size': 'E', 'code': '12480', 'category': 'RTU & Communication Panels',  'description': 'Carrier Terminal Panel', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'Carrier JB',	'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12440', 'category': 'RTU & Communication Panels',  'description': 'Termination Rack', 'dwg_each': 5, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12270', 'category': 'Junction & Demarcation Boxes',  'description': 'Metering 13.8kV PTs Conn', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12420', 'category': 'Junction & Demarcation Boxes',  'description': 'Fiber Splice Box', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12420', 'category': 'RTU & Communication Panels',  'description': 'Fiber Patch Panel', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12420', 'category': 'Panels',  'description': 'Marshalling Cabinets (60")', 'dwg_each': 2, 'qc_hrs': 1},
    {'size': 'A', 'code': '12530', 'category': 'Calcs',  'description': 'Voltage drop Cal', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'A', 'code': '12540', 'category': 'Calcs',  'description': 'AC/DC Load Cal', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Panels',  'description': 'AC Panel Wall Mounted for Control House AC', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Panels',  'description': 'Stand Alone AC Panel (Standard PM0101)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Panels',  'description': 'Outdoor Station Service AC Panels (new)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Panels',  'description': 'Stand Alone DC Panel, 125V DC (Standard PM0101)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Panels',  'description': 'Emergency Stand by Generator & DS Panel', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Connection Diagrams',  'description': 'SS Xfmr Connection Diagram (New)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Junction & Demarcation Boxes',  'description': 'Station Service Disribution Panel (3ph Outdoor)', 'dwg_each': 3, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Miscellaneous',  'description': 'UPS 120VAC with DC/AC inverter', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'Sudden Pressure J Box', 'dwg_each': 	1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': '500kV CT/CCVT J Box (3-Phase) High Voltage', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'CCVT J Box (3-Phase) High Voltage', 'dwg_each': 1, 'qc_hrs': 2},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'CCVT J Box (1-Phase) High Voltage', 'dwg_each': 1, 'qc_hrs': 1},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'PT/CCVT 230kV J Box (1-Phase) High Voltage', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'Bus CT Junction Box Removal', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'PT Distribution J Box (Indoor) PM2402 Option C', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'PT J Box (3-Phase) Low Voltage Outdoor', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12440', 'category': 'Miscellaneous',  'description': 'Transducer Cabinet Removal', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'PT/CCVT J Box Indoor', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12430', 'category': 'Junction & Demarcation Boxes',  'description': 'Wrap around 3200:5A MR CTs (3-Phase)', 'dwg_each': 2, 'qc_hrs': 1},
    {'size': 'E', 'code': '12430', 'category': 'Panels',  'description': 'Polarizing Potential Transfer Panel (Standard PM 3402)', 'dwg_each': 6, 'qc_hrs': 1},
    {'size': 'E', 'code': '12480', 'category': 'Panels',  'description': '34.5kV IDMC Switchgear Line-ups (SEL-387 or 787 & SEL-751A) (New)', 'dwg_each': 3, 'qc_hrs': 3},
    {'size': 'E', 'code': '12480', 'category': 'Miscellaneous',  'description': 'Transfer Switch (Demo)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Miscellaneous',  'description': 'AC Auto Transfer Switch', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12460', 'category': 'Calcs',  'description': 'Battery System (Battery, Rack, Maintenance Switch & Charger)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'A', 'code': '12450', 'category': 'Miscellaneous',  'description': 'Cable Pull List', 'dwg_each': 1, 'qc_hrs': 1},
    {'size': 'E', 'code': '12410', 'category': 'Miscellaneous',  'description': 'Control House Layout', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12440', 'category': 'Miscellaneous',  'description': 'Yard Lighting', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12210', 'category': 'Connection Diagrams',  'description': 'Xfmr Connection Diagram (New)', 'dwg_each': 1, 'qc_hrs': 4.25},
    {'size': 'E', 'code': '12210', 'category': 'Miscellaneous',  'description': 'Oil Monitoring',	'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12250', 'category': 'Connection Diagrams',  'description': 'Bkr Connection Diagram (Mod)', 'dwg_each': 1, 'qc_hrs': 1},
    {'size': 'E', 'code': '12250', 'category': 'Connection Diagrams',  'description': 'Bkr IPO Connection Diagram (NEW)', 'dwg_each': 1, 'qc_hrs': 1},
    {'size': 'E', 'code': '12240', 'category': 'Connection Diagrams',  'description': 'Circuit Switcher Connection Diagram (New)', 'dwg_each': 1, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12340', 'category': 'Calcs',  'description': 'Camera System', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12240', 'category': 'Miscellaneous',  'description': 'MOS Interlocks', 'dwg_each': 2, 'qc_hrs': 0.5},
    {'size': 'A', 'code': '12791', 'category': 'Miscellaneous',  'description': 'Powersafe Training & Safety Orientation Requirements (Hours)', 'dwg_each': 10, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12650', 'category': 'Miscellaneous',  'description': 'Demo Drawings', 'dwg_each': 27, 'qc_hrs': 0.5},
    {'size': 'E', 'code': '12650', 'category': 'Miscellaneous',  'description': 'Vendor Drawings', 'dwg_each': 18, 'qc_hrs': 0.5},
]

substation_drawings = [
    {'category': 'Electrical', 'size': '', 'code': '11010', 'description': 'Front-End Loading', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11010', 'description': 'Basis of Design Document', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11010', 'description': 'Pre-Design Review', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11010', 'description': 'Drawing List', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11010', 'description': 'Cover / Index', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11010', 'description': 'Switching One-Line', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11010', 'description': 'Preliminary Layout - EA Development', 'dwg_each': 4},
    {'category': 'Electrical', 'size': 'D', 'code': '11310', 'description': 'Foundation Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11330', 'description': 'Structure Modification Design',	'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Electrical Arrangement', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Demolition Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11410', 'description': 'Bus Calculations', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Bus Layout & Rating', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Electrical Profile', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Demolition Profiles', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Electrical Detail', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Sag Tension Profile', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11430', 'description': 'Grounding Calculations', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11430', 'description': 'Grounding Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11430', 'description': 'Grounding Details', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11430', 'description': 'Conduit Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11430', 'description': 'Conduit Stub-Up Details',	'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11430', 'description': 'Lighitng Calculations', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11430', 'description': 'Lighting Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11410', 'description': 'Shielding Calculations', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Shielding Plan', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11470', 'description': 'Control House Layout', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11470', 'description': 'Control House Exterior Elevations (Building Entrance Detail (x2))', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11470', 'description': 'Control House Interior Elevations', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Vendor Drawings', 'dwg_each': 4},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Standard Details', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Signage Drawing', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'D', 'code': '11410', 'description': 'Bill of Materials', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11410', 'description': 'Material Requisitions', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11410', 'description': 'Procurement Material Review', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11510', 'description': 'Study Support', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11520', 'description': 'Equipment Specifications (Entergy Appendix Update)', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11520', 'description': 'Construction Specifications', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11610', 'description': 'Miscellaneous', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11610', 'description': 'Rework / Recreate Station Drawings', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11710', 'description': 'Procurement Support', 'dwg_each': 1},
    {'category': 'Electrical', 'size': 'A', 'code': '11710', 'description': 'TPS Document', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11720', 'description': 'PM/PE Support', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11730', 'description': 'Construction Support', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11680', 'description': 'As-Built', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11660', 'description': 'Meetings', 'dwg_each': 1},
    {'category': 'Electrical', 'size': '', 'code': '11620', 'description': 'Quality Assurance', 'dwg_each': 1},

    {'category': 'Site', 'size': '', 'code': '11010', 'description': 'Front-End Loading', 'dwg_each': 1},
    {'category': 'Site', 'size': 'A', 'code': '11010', 'description': 'Basis of Design Document', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11010', 'description': 'Pre-Design Review', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11010', 'description': 'Cover / Index', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11010', 'description': 'Notes', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11010', 'description': 'Preliminary Layout - EA Development', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Existing Conditions', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Site Plan', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Demolition / Clearing & Grubbing Plan', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Roadway', 'dwg_each': 1},
    {'category': 'Site', 'size': 'A', 'code': '11210', 'description': 'Highway Permit Support', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Existing Pipe Removal / Relocation', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11210', 'description': 'Grading Design', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Grading Plan', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Grading Details', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Fence Layout', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Fence Details', 'dwg_each': 1},
    {'category': 'Site', 'size': 'A', 'code': '11210', 'description': 'Storm Water Calculations', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11250', 'description': 'Storm Water Pollution Prevention Plan (SWPPP)', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Standard Details', 'dwg_each': 1},
    {'category': 'Site', 'size': 'D', 'code': '11210', 'description': 'Vendor Drawings', 'dwg_each': 1},
    {'category': 'Site', 'size': 'A', 'code': '11210', 'description': 'Bill of Materials', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11210', 'description': 'Material Requisitions', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11210', 'description': 'Procurement Material Review', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11610', 'description': 'Miscellaneous', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11610', 'description': 'Rework / Recreate Station Drawings', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11710', 'description': 'Procurement Support', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11710', 'description': 'TPS Document', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11720', 'description': 'PM/PE Support', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11730', 'description': 'Construction Support', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11680', 'description': 'As-Built', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11660', 'description': 'Meetings', 'dwg_each': 1},
    {'category': 'Site', 'size': '', 'code': '11620', 'description': 'Quality Assurance', 'dwg_each': 1},

    {'category': 'Foundation', 'size': '', 'code': '11010', 'description': 'Front-End Loading', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'A', 'code': '11010', 'description': 'Basis of Design Document', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11010', 'description': 'Pre-Design Review', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11010', 'description': 'Cover / Index', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11010', 'description': 'Notes', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11010', 'description': 'Preliminary Layout - EA Development', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Foundation Plan', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Demolition Plan', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Pile Plan', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Foundation Details', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Foundation Details (Modification)', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'A', 'code': '11310', 'description': 'Foundation Calculations', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11330', 'description': 'Structure Modification Design', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11330', 'description': 'Structural Details / Review', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'A', 'code': '11330', 'description': 'Seismic Analysis', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Standard Details', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'D', 'code': '11310', 'description': 'Vendor Drawings', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'A', 'code': '11310', 'description': 'Bill of Materials', 'dwg_each': 1},
    {'category': 'Foundation', 'size': 'A', 'code': '11310', 'description': 'Material Requisitions', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11310', 'description': 'Procurement Material Review', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11610', 'description': 'Miscellaneous', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11610', 'description': 'Rework / Recreate Station Drawings', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11710', 'description': 'Procurement Support', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11710', 'description': 'TPS Document', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11720', 'description': 'PM/PE Support', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11730', 'description': 'Construction Support', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11680', 'description': 'As-Built', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11660', 'description': 'Meetings', 'dwg_each': 1},
    {'category': 'Foundation', 'size': '', 'code': '11620', 'description': 'Quality Assurance', 'dwg_each': 1},
]


ampirical_2019 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 54.00},
    {'classification': 'Construction Manager', 'rate': 157.00},
    {'classification': 'Design Manager', 'rate': 176.00},
    {'classification': 'Designer', 'rate': 102.00},
    {'classification': 'Director', 'rate': 184.00},
    {'classification': 'Drafter', 'rate': 66.00},
    {'classification': 'Engineer I', 'rate': 108.00},
    {'classification': 'Engineer II', 'rate': 118.00},
    {'classification': 'Engineer III', 'rate': 131.00},
    {'classification': 'Lead Engineer', 'rate': 168.00},
    {'classification': 'Principal Engineer', 'rate': 227.00},
    {'classification': 'Procurement Specialist', 'rate': 96.00},
    {'classification': 'Project Manager I', 'rate': 126.00},
    {'classification': 'Project Manager II', 'rate': 148.00},
    {'classification': 'Project Support Specialist', 'rate': 58.00},
    {'classification': 'Senior Designer', 'rate': 126.00},
    {'classification': 'Senior Drafter', 'rate': 82.00},
    {'classification': 'Senior Engineer', 'rate': 155.00},
    {'classification': 'Senior Project Manager', 'rate': 176.00},
    {'classification': 'Staff Engineer', 'rate': 179.00},
    {'classification': 'Technical Specialist', 'rate': 148.00},
    {'classification': 'Lead Procurement Specialist', 'rate': 110.00},
    {'classification': 'Document Control Specialist', 'rate': 84.00},
    {'classification': 'Safety Manager', 'rate': 1.00},
    {'classification': 'Senior Technical Specialist', 'rate': 157.00},
    {'classification': 'Project Controls Specialist', 'rate': 148.00},
    {'classification': 'Program Manager', 'rate': 187.00},
    {'classification': 'Project Manager', 'rate': 126.00},
    {'classification': 'Senior Safety Consultant', 'rate': 150.00},
    {'classification': 'Safety Consultant', 'rate': 114.00},
]

cleco_2018 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 51.00},
    {'classification': 'Construction Manager', 'rate': 113.00},
    {'classification': 'Design Manager', 'rate': 162.00},
    {'classification': 'Designer', 'rate': 95.00},
    {'classification': 'Director', 'rate': 173.00},
    {'classification': 'Drafter', 'rate': 62.00},
    {'classification': 'Engineer I', 'rate': 101.00},
    {'classification': 'Engineer II', 'rate': 112.00},
    {'classification': 'Engineer III', 'rate': 122.00},
    {'classification': 'Lead Engineer', 'rate': 157.00},
    {'classification': 'Principal Engineer', 'rate': 211.00},
    {'classification': 'Project Manager I', 'rate': 118.00},
    {'classification': 'Project Manager II', 'rate': 139.00},
    {'classification': 'Project Support Specialist', 'rate': 55.00},
    {'classification': 'Senior Designer', 'rate': 118.00},
    {'classification': 'Senior Drafter', 'rate': 78.00},
    {'classification': 'Senior Engineer', 'rate': 145.00},
    {'classification': 'Senior Project Manager', 'rate': 162.00},
    {'classification': 'Staff Engineer', 'rate': 173.00},
    {'classification': 'Technical Specialist', 'rate': 139.00},
]

dep_2018_2019 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 48.41},
    {'classification': 'Document Controller', 'rate': 55},
    {'classification': 'GIS/CAD Technician I', 'rate': 57.68},
    {'classification': 'CAD/Drafter', 'rate': 59.5},
    {'classification': 'Designer I', 'rate': 70},
    {'classification': 'Engineering Technologist I', 'rate': 74.16},
    {'classification': 'GIS/CAD Technician II', 'rate': 74.16},
    {'classification': 'Project Manager/Controls I', 'rate': 80},
    {'classification': 'Designer II', 'rate': 90},
    {'classification': 'Engineer I', 'rate': 93},
    {'classification': 'Engineering Technologist II', 'rate': 93.73},
    {'classification': 'Engineer', 'rate': 93.73},
    {'classification': 'Engineering Specialist III', 'rate': 104},
    {'classification': 'Engineering Technologist III', 'rate': 104.03},
    {'classification': 'Engineer II', 'rate': 104.03},
    {'classification': 'Project Manager/Controls II', 'rate': 115},
    {'classification': 'Engineer III', 'rate': 129},
    {'classification': 'Senior Engineer', 'rate': 129.78},
    {'classification': 'Senior Engineering Technologist', 'rate': 130.81},
    {'classification': 'Engineering Specialist IV', 'rate': 131},
    {'classification': 'Project Manager', 'rate': 142.14},
    {'classification': 'Lead Engineer', 'rate': 144.2},
    {'classification': 'Engineer IV', 'rate': 145},
    {'classification': 'Engineer V', 'rate': 155},
    {'classification': 'Principal Engineer', 'rate': 170.98},
    {'classification': 'Project Manager/Controls III', 'rate': 171},
    {'classification': 'Engineering Manager/Engineer VI', 'rate': 174},
]

entergy_2019 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 51.15},
    {'classification': 'Construction Manager', 'rate': 152.00},
    {'classification': 'Design Manager', 'rate': 165.02},
    {'classification': 'Designer', 'rate': 96.79},
    {'classification': 'Director', 'rate': 177.54},
    {'classification': 'Drafter', 'rate': 63.14},
    {'classification': 'Engineer I', 'rate': 103.40},
    {'classification': 'Engineer II', 'rate': 114.40},
    {'classification': 'Engineer III', 'rate': 125.18},
    {'classification': 'Lead Engineer', 'rate': 159.93},
    {'classification': 'Principal Engineer', 'rate': 216.58},
    {'classification': 'Project Manager I', 'rate': 119.53},
    {'classification': 'Project Manager II', 'rate': 142.67},
    {'classification': 'Project Support Specialist', 'rate': 55.55},
    {'classification': 'Senior Designer', 'rate': 119.67},
    {'classification': 'Senior Drafter', 'rate': 79.53},
    {'classification': 'Senior Engineer', 'rate': 148.06},
    {'classification': 'Senior Project Manager', 'rate': 165.02},
    {'classification': 'Senior Technical Specialist', 'rate': 155.55},
    {'classification': 'Staff Engineer', 'rate': 174.00},
    {'classification': 'Technical Specialist', 'rate': 142.67},
]

entergy_TE_2019 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 51.15},
    {'classification': 'Construction Manager', 'rate': 152.00},
    {'classification': 'Design Manager', 'rate': 165.02},
    {'classification': 'Designer', 'rate': 96.79},
    {'classification': 'Director', 'rate': 177.54},
    {'classification': 'Drafter', 'rate': 63.14},
    {'classification': 'Engineer I', 'rate': 103.40},
    {'classification': 'Engineer II', 'rate': 114.40},
    {'classification': 'Engineer III', 'rate': 125.18},
    {'classification': 'Lead Engineer', 'rate': 159.93},
    {'classification': 'Principal Engineer', 'rate': 216.58},
    {'classification': 'Project Manager I', 'rate': 119.53},
    {'classification': 'Project Manager II', 'rate': 142.67},
    {'classification': 'Project Support Specialist', 'rate': 55.55},
    {'classification': 'Senior Designer', 'rate': 119.67},
    {'classification': 'Senior Drafter', 'rate': 79.53},
    {'classification': 'Senior Engineer', 'rate': 148.06},
    {'classification': 'Senior Project Manager', 'rate': 165.02},
    {'classification': 'Senior Technical Specialist', 'rate': 155.55},
    {'classification': 'Staff Engineer', 'rate': 174.00},
    {'classification': 'Technical Specialist', 'rate': 142.67},
]

fpl_2017 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 51.00},
    {'classification': 'Construction Manager', 'rate': 116.00},
    {'classification': 'Design Manager', 'rate': 166.00},
    {'classification': 'Designer', 'rate': 96.00},
    {'classification': 'Director', 'rate': 174.00},
    {'classification': 'Drafter', 'rate': 62.00},
    {'classification': 'Engineer I', 'rate': 102.10},
    {'classification': 'Engineer II', 'rate': 112.00},
    {'classification': 'Engineer III', 'rate': 123.00},
    {'classification': 'Lead Engineer', 'rate': 158.00},
    {'classification': 'Principal Engineer', 'rate': 214.00},
    {'classification': 'Project Manager I', 'rate': 119.00},
    {'classification': 'Project Manager II', 'rate': 140.00},
    {'classification': 'Project Support Specialist', 'rate': 55.00},
    {'classification': 'Senior Designer', 'rate': 118.00},
    {'classification': 'Senior Drafter', 'rate': 78.00},
    {'classification': 'Senior Engineer', 'rate': 146.00},
    {'classification': 'Senior Project Manager', 'rate': 166.00},
    {'classification': 'Staff Engineer', 'rate': 169.00},
    {'classification': 'Technical Specialist', 'rate': 140.00},
]

muscatatuck = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 51.00},
    {'classification': 'Construction Manager', 'rate': 116.00},
    {'classification': 'Design Manager', 'rate': 166.00},
    {'classification': 'Designer', 'rate': 96.00},
    {'classification': 'Director', 'rate': 174.00},
    {'classification': 'Drafter', 'rate': 62.00},
    {'classification': 'Engineer I', 'rate': 102.10},
    {'classification': 'Engineer II', 'rate': 112.00},
    {'classification': 'Engineer III', 'rate': 123.00},
    {'classification': 'Lead Engineer', 'rate': 158.00},
    {'classification': 'Principal Engineer', 'rate': 214.00},
    {'classification': 'Procurement Specialist', 'rate': 75.00},
    {'classification': 'Project Manager I', 'rate': 119.00},
    {'classification': 'Project Manager II', 'rate': 140.00},
    {'classification': 'Project Support Specialist', 'rate': 55.00},
    {'classification': 'Senior Designer', 'rate': 118.00},
    {'classification': 'Senior Drafter', 'rate': 78.00},
    {'classification': 'Senior Engineer', 'rate': 146.00},
    {'classification': 'Senior Project Manager', 'rate': 166.00},
    {'classification': 'Staff Engineer', 'rate': 169.00},
    {'classification': 'Technical Specialist', 'rate': 140.00},
    {'classification': 'Training & Compliance Coord', 'rate': 51.00},
    {'classification': 'Project Scheduler', 'rate': 135.00},
    {'classification': 'Project Coordinator', 'rate': 120.00},
]

pge_11_01_2018 = [
    {'classification': 'None', 'rate': 0.00},
    {'classification': 'Clerk', 'rate': 50.20},
    {'classification': 'Design Manager', 'rate': 215.50},
    {'classification': 'Designer', 'rate': 82.56},
    {'classification': 'Drafter', 'rate': 55.99},
    {'classification': 'Engineer I', 'rate': 100.47},
    {'classification': 'Engineer II', 'rate': 110.12},
    {'classification': 'Engineer III', 'rate': 117.53},
    {'classification': 'Engineering Expert', 'rate': 215.50},
    {'classification': 'Lead Engineer', 'rate': 141.96},
    {'classification': 'Principal Engineer', 'rate': 199.19},
    {'classification': 'Senior Construction Manager', 'rate': 167.45},
    {'classification': 'Project Manager', 'rate': 144.56},
    {'classification': 'Senior Designer', 'rate': 115.93},
    {'classification': 'Senior Drafter', 'rate': 55.99},
    {'classification': 'Senior Engineer', 'rate': 141.96},
    {'classification': 'Senior Project Manager', 'rate': 195.69},
    {'classification': 'Senior Technical Specialist', 'rate': 215.50},
    {'classification': 'Staff Engineer', 'rate': 215.50},
    {'classification': 'Technical Specialist', 'rate': 115.93},
]

resources = {'Ampirical 2019': ampirical_2019,
             'Cleco 2018': cleco_2018,
             # 'Dep 2018-19': dep_2018_2019,
             'Entergy 2019': entergy_2019,
             'Entergy T&E 2019': entergy_TE_2019,
             'FPL 2017': fpl_2017,
             'Muscatatuck': muscatatuck,
             'PG&E 11/01/2018': pge_11_01_2018
            }

relay_settings = [
    {'description': 'Line - SEL-421', 'cost_per_relay': 3500, 'hours_per_device': 10, 'category': 'Settings'},
    {'description': 'Line - SEL-411L', 'cost_per_relay': 5000, 'hours_per_device': 20, 'category': 'Settings'},
    {'description': 'Line - SEL-311C', 'cost_per_relay': 5000, 'hours_per_device': 40, 'category': 'Settings'},
    {'description': 'Breaker - SEL-451-5', 'cost_per_relay': 3500, 'hours_per_device': 20, 'category': 'Settings'},
    {'description': 'Breaker - SEL-451 Mod', 'cost_per_relay': 2500, 'hours_per_device': 5, 'category': 'Settings'},
    {'description': 'XFMR Diff - SEL-387-5', 'cost_per_relay': 2000, 'hours_per_device': 15, 'category': 'Settings'},
    {'description': 'XFMR Diff - SEL-487E', 'cost_per_relay': 2500, 'hours_per_device': 30, 'category': 'Settings'},
    {'description': 'XFMR Diff - SEL-587', 'cost_per_relay': 2500, 'hours_per_device': 20, 'category': 'Settings'},
    {'description': 'Meters', 'cost_per_relay': 500, 'hours_per_device': 5, 'category': 'Settings'},
    {'description': 'Bus Diff - SEL-487B', 'cost_per_relay': 2500, 'hours_per_device': 8, 'category': 'Settings'},
    {'description': 'Coordination Study', 'cost_per_relay': 5000, 'hours_per_device': 10, 'category': 'Studies'},  # just made up the hours_per_device on this one
    {'description': 'RTU/Annunciator Configuration (1=small, 1.5=med, 2=larger)', 'cost_per_relay': 5000, 'hours_per_device': 36,  'category': 'Studies'},
    {'description': 'Arc Flash Evaluation for 35kV Switchgear Line-up', 'cost_per_relay': 5000, 'hours_per_device': 36,  'category': 'Studies'},
]

geo_techs = [
    {'description': 'Soil Boring', 'cost_per_geo_tech': 8000},
    {'description': 'Survey', 'cost_per_geo_tech': 6000},
    {'description': 'Soil Resistivity', 'cost_per_geo_tech': 3000},
    {'description': 'Grid Impedance', 'cost_per_geo_tech': 3000},
]


drawing_time = [{"activity_type":"substation",
                 "engineer_new_drawing": 4, "engineer_retro_drawing": 2,
                 "designer_new_drawing": 6, "designer_retro_drawing": 4,
                 "drafter_new_drawing": 6, "drafter_retro_drawing": 4,
                 "a": .25, "b": .5, "c": .65, "d": 1, "e": 1
                 },
                 {"activity_type":"relay",
                  "engineer_new_drawing": 6.75, "engineer_retro_drawing": 1.5,
                  "designer_new_drawing": 0, "designer_retro_drawing": 0,
                  "drafter_new_drawing": 4.25, "drafter_retro_drawing": 2,
                  "a": .25, "b": .5, "c": .65, "d": 1, "e": 1
                  }]

# man_loading = [
#     {'resource': 'principal_engineer','IFA': 2.88, 'IFC': .16},
#     {'resource': 'management','IFA': 0, 'IFC': 0},
#     {'resource': 'design_manager','IFA': 23.08, 'IFC': 1.28},
#     {'resource': 'project_manager', 'IFA': 14.42, 'IFC': .08},
#     {'resource': 'director', 'IFA': 1.44, 'IFC': .08},
#     {'resource': 'staff_engineer', 'IFA': 1.44, 'IFC': .08},
#     {'resource': 'project_engineer', 'IFA': 1.44, 'IFC': .08},
#     {'resource': 'construction_manager', 'IFA': 1.44, 'IFC': .08},
#     {'resource': 'administrative_assistant', 'IFA': 1.44, 'IFC': .08},
#     {'resource': 'engineer_III', 'IFA': 858.6, 'IFC': 47.7},
#     {'resource': 'engineer_II', 'IFA': 858.6, 'IFC': 47.7},
# ]



add_wbs_codes(wbs_codes)
add_relay_drawings(relay_drawings)
add_substation_drawings(substation_drawings)
add_resources(resources)
add_relay_settings(relay_settings)
# add_drawing_time(drawing_time)
add_geo_tech(geo_techs)

from edc_lab import Process, ProcessingProfile
from edc_lab.lab import RequisitionPanel, LabProfile
from edc_lab.aliquot_types import wb, pl, bc, serum, fbc

wb.add_derivatives(bc, pl, serum, fbc, wb)

# processing
whole_blood_processing = ProcessingProfile(
    name="whole_blood_store", aliquot_type=wb)
wb_process = Process(aliquot_type=wb, aliquot_count=2)
whole_blood_processing.add_processes(wb_process)

cd4_processing = ProcessingProfile(name="CD4", aliquot_type=wb)

fbc_processing = ProcessingProfile(name="FBC", aliquot_type=wb)

chemistry_processing = ProcessingProfile(name="Chem", aliquot_type=wb)

viral_load_processing = ProcessingProfile(name="viral_load", aliquot_type=wb)
vl_pl_process = Process(aliquot_type=pl, aliquot_count=4)
vl_bc_process = Process(aliquot_type=bc, aliquot_count=2)
viral_load_processing.add_processes(vl_pl_process, vl_bc_process)

# panels
wb_panel = RequisitionPanel(
    name="wb_storage",
    verbose_name="Whole Blood Storage",
    processing_profile=whole_blood_processing,
)


cd4_panel = RequisitionPanel(
    name="cd4", verbose_name="CD4", processing_profile=cd4_processing
)

viral_load_panel = RequisitionPanel(
    name="vl", verbose_name="Viral Load", processing_profile=viral_load_processing
)

fbc_panel = RequisitionPanel(
    name="fbc", verbose_name="Full Blood Count", processing_profile=fbc_processing
)

chemistry_panel = RequisitionPanel(
    name="chemistry",
    verbose_name="Creat, Urea, Elec",
    processing_profile=chemistry_processing,
)


lab_profile = LabProfile(
    name="lab_profile", requisition_model="example_subject.subjectrequisition"
)

lab_profile.add_panel(cd4_panel)
lab_profile.add_panel(chemistry_panel)
lab_profile.add_panel(fbc_panel)
lab_profile.add_panel(viral_load_panel)
lab_profile.add_panel(wb_panel)

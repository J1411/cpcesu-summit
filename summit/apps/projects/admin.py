from django.contrib import admin

from .models import Project, File, Location, Modification, ModFile


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__',
                    'award_office',
                    'budget',
                    'cesu_unit',
                    'description',
                    'discipline',
                    'exec_start_date',
                    'federal_agency',
                    'field_of_science',
                    'final_report',
                    'fiscal_year',
                    'location',
                    'init_start_date',
                    'monitoring',
                    'notes',
                    'num_of_students',
                    'p_num',
                    'partner',
                    'pp_i',
                    'project_manager',
                    'project_title',
                    'r_d',
                    'reviewed',
                    'sci_method',
                    'sensitive',
                    'short_summary',
                    'src_of_funding',
                    'staff_member',
                    'status',
                    'tech_rep',
                    'tent_end_date',
                    'tent_start_date',
                    'type',
                    'fed_poc',
                    'funding',
                    'comm_start_date',
                    'task_agreement_start_date',
                    'actual_start',
                    'actual_end',
                    'perm_share',
                    'award_amt',
                    'alt_coord',
                    'req_iacuc',
                    'youth_vets',
                    'field_of_science_sub',
                    'job_id',
                    'legacy_award_number',
                    'legacy_match_amount',
                    'legacy_ca_account_number',
                    'legacy_account_number',
                    'legacy_area_org',
                    'legacy_pwe',
                    'legacy_project_products',
                    'legacy_received_report_date',
                    'legacy_sent_to_tic',)
    search_fields = ('award_office',
                    'budget',
                    'cesu_unit',
                    'description',
                    'discipline',
                    'exec_start_date',
                    'federal_agency',
                    'field_of_science',
                    'final_report',
                    'fiscal_year',
                    'location',
                    'init_start_date',
                    'monitoring',
                    'notes',
                    'num_of_students',
                    'p_num',
                    'partner',
                    'pp_i',
                    'project_manager',
                    'project_title',
                    'r_d',
                    'reviewed',
                    'sci_method',
                    'sensitive',
                    'short_summary',
                    'src_of_funding',
                    'staff_member',
                    'status',
                    'tech_rep',
                    'tent_end_date',
                    'tent_start_date',
                    'type',
                    'fed_poc',
                    'funding',
                    'comm_start_date',
                    'task_agreement_start_date',
                    'actual_start',
                    'actual_end',
                    'perm_share',
                    'award_amt',
                    'alt_coord',
                    'req_iacuc',
                    'youth_vets',
                    'field_of_science_sub',
                    'job_id',
                    'legacy_award_number',
                    'legacy_match_amount',
                    'legacy_ca_account_number',
                    'legacy_account_number',
                    'legacy_area_org',
                    'legacy_pwe',
                    'legacy_project_products',
                    'legacy_received_report_date',
                    'legacy_sent_to_tic',)


class FileAdmin(admin.ModelAdmin):
    list_display = ('project', 'file')


admin.site.register(Project, ProjectAdmin)
admin.site.register(File)
admin.site.register(Modification)
admin.site.register(ModFile)
admin.site.register(Location)

# Copyright 2018 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Project API",
    "summary": "Expose a json-rpc like API on top of base_rest",
    "version": "14.0.1.0.0",
    "category": "Project Management",
    "author": "Akretion",
    "website": "https://github.com/akretion/support",
    "license": "AGPL-3",
    "depends": [
        "auth_api_key",
        "base_rest",
        "project",
        "project_task_default_stage",
        "project_tag",
        "project_estimate_step",
    ],
    "data": ["views/project_view.xml", "views/partner_view.xml"],
    "demo": ["demo/partner_demo.xml", "demo/project_demo.xml"],
    "installable": True,
    "application": True,
}

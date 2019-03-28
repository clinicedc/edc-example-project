from edc_reference import ReferenceModelConfig, site_reference_configs


def register_to_site_reference_configs():
    site_reference_configs.registry = {}

    reference = ReferenceModelConfig(name="example_main.CrfOne", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfTwo", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfThree", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfFour", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfFive", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfSix", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(name="example_main.CrfSeven", fields=["f1"])
    site_reference_configs.register(reference)

    reference = ReferenceModelConfig(
        name="example_main.CrfMissingManager", fields=["f1"]
    )
    site_reference_configs.register(reference)

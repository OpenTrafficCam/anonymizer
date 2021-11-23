import anonymizer.bin.anonymize as anonymize
from gui import Mainwindow


# Define parameters
# input_pics = r"C:\Users\Baerwolff\trash\anonymizer_pics\input_pics"
# output_pics = r"C:\Users\Baerwolff\trash\anonymizer_pics\output_pics"
image_extensions = "jpg,png"
face_threshold = 0.25  # Must be in [0.001, 1.0]
plate_threshold = 0.25  # Must be in [0.001, 1.0]
obfuscation_parameters = "41,2,9"

# Run program
anonymize.main(
    input_path=None,
    image_output_path=None,
    image_extensions=image_extensions,
    face_threshold=face_threshold,
    plate_threshold=plate_threshold,
    write_json=True,
    obfuscation_parameters=obfuscation_parameters,
)

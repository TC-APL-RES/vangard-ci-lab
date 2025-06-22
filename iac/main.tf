cat <<EOF > iac/main.tf
resource "aws_s3_bucket" "bad_example" {
  bucket = "unsecure-bucket"
  acl    = "public-read"
}
EOFX

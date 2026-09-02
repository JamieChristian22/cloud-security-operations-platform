output "vpc_id" { value=aws_vpc.this.id }
output "private_subnet_ids" { value={for k,v in aws_subnet.private:k=>v.id} }
output "audit_bucket" { value=aws_s3_bucket.audit.id }

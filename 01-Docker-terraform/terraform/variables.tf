variable "credentials_file" {
  description = "Path to the GCP credentials JSON file."
  type        = string
  default     = "./keys/my-creds.json"
}



variable "project_id" {
  description = "The GCP project ID where resources will be created."
  type        = string
  default     = "terraform-2-496114"
}


variable "region" {
  description = "The region where resources will be created."
  type        = string
  default     = "europe-west1"
}


variable "location" {
  description = "The location for the BigQuery dataset and GCS bucket."
  type        = string
  default     = "EU"
}


variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset to create."
  type        = string
  default     = "demo_dataset"
}


variable "gcs_bucket_name" {
  description = "The name of the GCS bucket to create."
  type        = string
  default     = "terraform-2-496114-terra-bucket"
}


variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  type        = string
  default     = "STANDARD"
}

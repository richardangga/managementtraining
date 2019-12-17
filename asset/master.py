from odoo import api, fields, models, _
import time

class Datauser(models.Model):
	_name = 'management.datauser'

	username_data = fields.Char(string="Username",required=True)
	identitas_data = fields.Char(string="Identitas",required=False)
	namalengkap_data = fields.Char(string="Nama Lengkap",required=False)
	level_data = fields.Char(string="Level",required=False)
	blokir_data = fields.Selection(string="Blokir",selection=[('Y','Yes'),('N','No')],default='N',required=True)
	pemandu_data = fields.Selection(string="Pemandu",selection=[('Y','Yes'),('N','No')],required=False)
	pengelola_data = fields.Selection(string="Pengelola",selection=[('Y','Yes'),('N','No')],default='N',required=True)
	tempadmin_data = fields.Selection(string="Temp Admin",selection=[('Y','Yes'),('N','No')],required=False)

class Lokasi(models.Model):
	_name = 'management.lokasi'
	_rec_name = 'lokasi'

	no_lokasi = fields.Integer(string="No Lokasi",required=True)
	lokasi = fields.Char(string="Lokasi",required=True)

class Ruang(models.Model):
	_name = 'management.ruang'
	# _rec_name = 'ruang'

	id_lokasi = fields.Many2one(string="Lokasi",comodel_name='management.lokasi',required=True)
	no_ruang = fields.Integer(string="No Ruang",required=True)
	name = fields.Char(string="Nama Ruang",required=True)

class Subruang(models.Model):
	_name = 'management.subruang'
	# _rec_name = 'subruang'

	id_ruang = fields.Many2one(string="Ruang",comodel_name='management.ruang',required=True)
	no_subruang = fields.Integer(string="No Sub Ruang",required=True)
	name = fields.Char(string="Nama Sub Ruang",required=True)

class Merk(models.Model):
	_name = 'management.merk'

	nama_merk = fields.Char(string="Merk",required=True)

class Unit(models.Model):
	_name = 'management.unit'

	no_unit = fields.Char(string="No Unit",required=True)
	name = fields.Char(string="Nama Unit",required=True)

class Subunit(models.Model):
	_name = 'management.subunit'

	id_subunit = fields.Many2one(string="KodeGolongan Perangkat",comodel_name='management.unit',required=True)
	no_subunit = fields.Integer(string="No Sub Unit",required=True)
	nama_subunit = fields.Char(string="Nama Sub Unit",required=True)

class KodePerangkat(models.Model):
	_name = 'management.kodeperangkat'

	no_perangkat = fields.Integer(string="No Perangkat",required=True)
	name = fields.Char(string="Golongan Perangkat",required=True)

class KodeGolPerangkat(models.Model):
	_name = 'management.kodegolperangkat'

	id_kelperangkat = fields.Many2one(string="Kode Golongan Perangkat",comodel_name='management.kodeperangkat',required=True)
	no_kelperangkat =  fields.Integer(string="No Kelompok Perangkat",required=True)
	nama_kelperangkat = fields.Char(string="Nama Kelompok Perangkat",required=True)

class PerangkatDC(models.Model):
	_name = 'management.perangkatdc'

	skpd_pemilik = fields.Char(string="SKPD/UKPD Pemilik/Penanggung Jawab",required=True)
	ruang_posisi = fields.Many2one(string="Ruang/Posisi",comodel_name='management.ruang',required=True)
	no_regsn = fields.Char(string="No.Reg/SN/SP",required=True)
	merk_modeltype = fields.Char(string="Merk/Model/Type",required=True)
	spesifikasi = fields.Text(string="Spesifikasi",required=False)
	fungsi = fields.Text(string="Fungsi",required=False)
	visit = fields.Integer(string="Visit",required=True)
	note = fields.Text(string="Note",required=False)

class PerangkatNonDC(models.Model):
	_name = 'management.perangkatnondc'

	skpd_pemiliknondc = fields.Char(string="SKPD/UKPD Pemilik/Penanggung Jawab",required=True)
	ruang_posisinondc = fields.Char(string="Ruang/Posisi",required=True)
	no_regsnnondc = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypenondc = fields.Char(string="Merk/Model/Type",required=True)
	spesifikasinondc = fields.Text(string="Spesifikasi",required=False)
	fungsinondc = fields.Text(string="Fungsi",required=False)
	visitnondc = fields.Integer(string="Visit",required=True)
	notenondc = fields.Text(string="Note",required=False)

class PowerDistribution(models.Model):
	_name = 'management.powerdistribution'

	ruang_power = fields.Many2one(string="Ruang",comodel_name='management.ruang',required=True)
	posisi_power = fields.Many2one(string="Posisi",comodel_name='management.subruang',required=True)
	no_regsnpower = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypepower = fields.Text(string="Merk/Model/Type",required=False)
	fungsipower = fields.Text(string="Fungsi",required=False)
	koneksipower = fields.Char(string="Koneksi Listrik",required=False)
	distribusipower = fields.Integer(string="Distribusi",required=True)
	visitpower = fields.Integer(string="Visit",required=True)
	notepower = fields.Text(string="Note",required=False)

class LanDistribution(models.Model):
	_name = 'management.landistribution'

	ruang_lan = fields.Many2one(string="Ruang",comodel_name='management.ruang',required=True)
	posisi_lan = fields.Many2one(string="Posisi",comodel_name='management.subruang',required=True)
	no_regsnlan = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypelan = fields.Text(string="Merk/Model/Type",required=False)
	fungsilan = fields.Text(string="Fungsi",required=False)
	koneksilan = fields.Char(string="Koneksi LAN",required=False)
	distribusilan = fields.Integer(string="Distribusi",required=True)
	visitlan = fields.Integer(string="Visit",required=True)
	notelan = fields.Text(string="Note",required=False)

class Capacity(models.Model):
	_name = 'management.capacity'

	rack_capacity = fields.Char(string="Rack",required=True)
	used_capacity = fields.Integer(string="Used",required=True)
	available_capacity = fields.Integer(string="Available",required=True)

class UtilisasiPerangkatDC(models.Model):
	_name = 'management.utilisasiperangkatdc'

	osmerkutilisasi = fields.Text(string="OS/Merk/Model/Type/IP",required=True)
	cpuutilisasi = fields.Integer(string="CPU",required=True)
	ramutilisasi = fields.Char(string="RAM",required=True)
	diskutilisasi = fields.Char(string="DISK",required=True)
	traficutilisasi = fields.Integer(string="Traffic In/Out",required=True)
	fungsiutilisasi = fields.Text(string="Fungsi/Note",required=False)

class DocumentRecruitment(models.Model):
	_name = 'document.recruitment'

	docrecnama = fields.Char(string="Nama",required=True)
	docreckode = fields.Char(string="Kode",required=True)
	docreckelamin = fields.Selection(string="Kelamin",selection=[('L','Laki-Laki'),('P','Perempuan')],required=True)
	docrecusia = fields.Char(string="Usia",required=True)
	docrecpendidikan = fields.Char(string="Pendidikan",required=True)
	docrectelp = fields.Char(string="Telp/HP",required=True)
	docrecemail = fields.Char(string="Email",required=True)
	docnamefile = fields.Char(string="File Name")
	docrecfile = fields.Binary(string="File",required=False)
	docrecpengalaman = fields.Selection(string="Pengalaman",selection=[('Y','Yes'),('N','No')],default='N',required=True)
	docreccatatan = fields.Text(string="Catatan",required=False)

class DocumentSop(models.Model):
	_name = 'document.sop'

	docsopcode = fields.Char(string="Code",required=True)
	docsopname = fields.Char(string="SOP Name",required=True)
	docsopdateissue = fields.Date(string="Date Issued",default=lambda self: time.strftime("%Y-%m-%d"),required=False)
	docsopdatereview = fields.Date(string="Date Reviewed",default=lambda self: time.strftime("%Y-%m-%d"),required=False)
	docsopdaterevised = fields.Date(string="Date Revised",default=lambda self: time.strftime("%Y-%m-%d"),required=False)

class DocumentBcp(models.Model):
	_name = 'document.bcp'

	docbcpcode = fields.Char(string="Code",required=True)
	docbcpname = fields.Char(string="BCP Name",required=True)
	docbcpdateissue = fields.Date(string="Date Issued",default=lambda self: time.strftime("%Y-%m-%d"),required=False)
	docbcpdatereview = fields.Date(string="Date Reviewed",default=lambda self: time.strftime("%Y-%m-%d"),required=False)
	docbcpdaterevised = fields.Date(string="Date Revised",default=lambda self: time.strftime("%Y-%m-%d"),required=False)

class DocumentBerita(models.Model):
	_name = 'document.berita'

	docberitajudul = fields.Char(string="Judul",required=True)
	docberitaposting = fields.Date(string="Tgl Posting",default=lambda self: time.strftime("%Y-%m-%d"),required=True)
	docberitapublish = fields.Selection(string="Publish",selection=[('Y','Yes'),('N','No')],default='N',required=True)

class DocumentAgenda(models.Model):
	_name = 'document.agenda'

	docagendatema = fields.Char(string="Tema",required=True)
	docagendamulai = fields.Date(string="Tgl Mulai",default=lambda self: time.strftime("%Y-%m-%d"),required=True)
	docagendaselesai = fields.Date(string="Tgl Selesai",default=lambda self: time.strftime("%Y-%m-%d"),required=True)
	
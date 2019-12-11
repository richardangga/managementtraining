from odoo import api, fields, models, _
import time

class Datauser(models.Model):
	_name = 'management.datauser'

	username_data = fields.Char(string="Username",required=True)
	identitas_data = fields.Integer(string="Identitas",required=False)
	namalengkap_data = fields.Char(string="Nama Lengkap",required=False)
	level_data = fields.Char(string="Level",required=False)
	blokir_data = fields.Char(string="Blokir",required=True)
	pemandu_data = fields.Char(string="Pemandu",required=False)
	pengelola_data = fields.Char(string="Pengelola",required=True)
	tempadmin_data = fields.Char(string="Temp Admin",required=False)

class Lokasi(models.Model):
	_name = 'management.lokasi'
	_rec_name = 'lokasi'

	no_lokasi = fields.Integer(string="No Lokasi",required=True)
	lokasi = fields.Char(string="Lokasi",required=True)

class Ruang(models.Model):
	_name = 'management.ruang'
	# _rec_name = 'ruang'

	id_lokasi = fields.Many2one(string="Lokasi",comodel_name='management.lokasi',)
	no_ruang = fields.Integer(string="No Ruang",required=True)
	nama_ruang = fields.Char(string="Nama Ruang",required=True)

class Subruang(models.Model):
	_name = 'management.subruang'
	# _rec_name = 'subruang'

	id_ruang = fields.Many2one(string="Ruang",comodel_name='management.ruang')
	no_subruang = fields.Integer(string="No Sub Ruang",required=True)
	nama_subruang = fields.Char(string="Nama Sub Ruang",required=True)

class Merk(models.Model):
	_name = 'management.merk'

	nama_merk = fields.Char(string="Merk",required=True)

class Unit(models.Model):
	_name = 'management.unit'

	no_unit = fields.Integer(string="No Unit",required=True)
	nama_unit = fields.Char(string="Nama Unit",required=True)

class Subunit(models.Model):
	_name = 'management.subunit'

	id_subunit = fields.Many2one(string="KodeGolongan Perangkat",comodel_name='management.unit')
	no_subunit = fields.Integer(string="No Sub Unit",required=True)
	nama_subunit = fields.Char(string="Nama Sub Unit",required=True)

class KodePerangkat(models.Model):
	_name = 'management.kodeperangkat'

	no_perangkat = fields.Integer(string="No Perangkat",required=True)
	gol_perangkat = fields.Char(string="Golongan Perangkat",required=True)

class KodeGolPerangkat(models.Model):
	_name = 'management.kodegolperangkat'

	id_kelperangkat = fields.Many2one(string="Kode Golongan Perangkat",comodel_name='management.kodeperangkat')
	no_kelperangkat =  fields.Integer(string="No Kelompok Perangkat",required=True)
	nama_kelperangkat = fields.Char(string="Nama Kelompok Perangkat",required=True)



class PerangkatDC(models.Model):
	_name = 'management.perangkatdc'

	skpd_pemilik = fields.Char(string="SKPD/UKPD Pemilik/Penanggung Jawab",required=True)
	ruang_posisi = fields.Char(string="Ruang/Posisi",required=True)
	no_regsn = fields.Char(string="No.Reg/SN/SP",required=True)
	merk_modeltype = fields.Char(string="Merk/Model/Type",required=True)
	spesifikasi = fields.Char(string="Spesifikasi",required=False)
	fungsi = fields.Char(string="Fungsi",required=False)
	visit = fields.Integer(string="Visit",required=True)
	note = fields.Char(string="Note",required=False)

class PerangkatNonDC(models.Model):
	_name = 'management.perangkatnondc'

	skpd_pemiliknondc = fields.Char(string="SKPD/UKPD Pemilik/Penanggung Jawab",required=True)
	ruang_posisinondc = fields.Char(string="Ruang/Posisi",required=True)
	no_regsnnondc = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypenondc = fields.Char(string="Merk/Model/Type",required=True)
	spesifikasinondc = fields.Char(string="Spesifikasi",required=False)
	fungsinondc = fields.Char(string="Fungsi",required=False)
	visitnondc = fields.Integer(string="Visit",required=True)
	notenondc = fields.Char(string="Note",required=False)

class PowerDistribution(models.Model):
	_name = 'management.powerdistribution'

	ruang_power = fields.Char(string="Ruang",required=True)
	posisi_power = fields.Char(string="Posisi",required=True)
	no_regsnpower = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypepower = fields.Char(string="Merk/Model/Type",required=True)
	fungsipower = fields.Char(string="Fungsi",required=True)
	koneksipower = fields.Char(string="Koneksi Listrik",required=True)
	distribusipower = fields.Integer(string="Distribusi",required=True)
	visitpower = fields.Integer(string="Visit",required=True)
	notepower = fields.Char(string="Note",required=False)

class LanDistribution(models.Model):
	_name = 'management.landistribution'

	ruang_lan = fields.Char(string="Ruang",required=True)
	posisi_lan = fields.Char(string="Posisi",required=True)
	no_regsnlan = fields.Char(string="No.Reg/SN",required=True)
	merk_modeltypelan = fields.Char(string="Merk/Model/Type",required=False)
	fungsilan = fields.Char(string="Fungsi",required=False)
	koneksilan = fields.Char(string="Koneksi LAN",required=False)
	distribusilan = fields.Integer(string="Distribusi",required=True)
	visitlan = fields.Integer(string="Visit",required=True)
	notelan = fields.Char(string="Note",required=False)

class Capacity(models.Model):
	_name = 'management.capacity'

	rack_capacity = fields.Char(string="Rack",required=True)
	used_capacity = fields.Integer(string="Used",required=True)
	available_capacity = fields.Integer(string="Available",required=True)

class UtilisasiPerangkatDC(models.Model):
	_name = 'management.utilisasiperangkatdc'

	osmerkutilisasi = fields.Char(string="OS/Merk/Model/Type/IP",required=True)
	cpuutilisasi = fields.Char(string="CPU",required=True)
	ramutilisasi = fields.Char(string="RAM",required=True)
	diskutilisasi = fields.Char(string="DISK",required=True)
	traficutilisasi = fields.Integer(string="Traffic In/Out",required=True)
	fungsiutilisasi = fields.Char(string="Fungsi/Note",required=True)

class DocumentRecruitment(models.Model):
	_name = 'document.recruitment'

	docrecnama = fields.Char(string="Nama",required=True)
	docreckode = fields.Char(string="Kode",required=True)
	docreckelamin = fields.Char(string="Kelamin",required=True)
	docrecusia = fields.Char(string="Usia",required=True)
	docrecpendidikan = fields.Char(string="Pendidikan",required=True)
	docrectelp = fields.Char(string="Telp/HP",required=True)
	docrecemail = fields.Char(string="Email",required=True)
	docrecfile = fields.Char(string="File",required=True)
	docrecpengalaman = fields.Char(string="Pengalaman",required=True)
	docreccatatan = fields.Char(string="Catatan",required=True)

class DocumentSop(models.Model):
	_name = 'document.sop'

	docsopcode = fields.Char(string="Code",required=True)
	docsopname = fields.Char(string="SOP Name",required=True)
	docsopdateissue = fields.Char(string="Date Issued",required=False)
	docsopdatereview = fields.Char(string="Date Reviewed",required=False)
	docsopdaterevised = fields.Char(string="Date Revised",required=False)

class DocumentBcp(models.Model):
	_name = 'document.bcp'

	docbcpcode = fields.Char(string="Code",required=True)
	docbcpname = fields.Char(string="BCP Name",required=True)
	docbcpdateissue = fields.Char(string="Date Issued",required=False)
	docbcpdatereview = fields.Char(string="Date Reviewed",required=False)
	docbcpdaterevised = fields.Char(string="Date Revised",required=False)

class DocumentBerita(models.Model):
	_name = 'document.berita'

	docberitajudul = fields.Char(string="Judul",required=True)
	docberitaposting = fields.Char(string="Tgl Posting",required=True)
	docberitapublish = fields.Char(string="Publish",required=True)

class DocumentAgenda(models.Model):
	_name = 'document.agenda'

	docagendatema = fields.Char(string="Tema",required=True)
	docagendamulai = fields.Char(string="Tgl Mulai",required=True)
	docagendaselesai = fields.Char(string="Tgl Selesai",required=True)
	
# Modules always contain just 32-bit code
%define _libdir %{_exec_prefix}/lib

# 64bit intel machines use 32bit boot loader
# (We cannot just redefine _target_cpu, as we'd get i386.rpm packages then)
%ifarch x86_64
%define _target_platform i386-%{_vendor}-%{_target_os}%{?_gnu}
%endif
# sparc is always compiled 64 bit
%ifarch %{sparc}
%define _target_platform sparc64-%{_vendor}-%{_target_os}%{?_gnu}
%endif

%if ! 0%{?efi}

%global efiarchs %{ix86} x86_64 ia64

%ifarch %{ix86}
%global grubefiarch i386-efi
%global grubefiname grubia32.efi
%global grubeficdname gcdia32.efi
%endif
%ifarch x86_64
%global grubefiarch %{_arch}-efi
%global grubefiname grubx64.efi
%global grubeficdname gcdx64.efi
%endif

%if 0%{?rhel}
%global efidir redhat
%endif
%if 0%{?fedora}
%global efidir fedora
%endif

%endif

%global tarversion 2.00
%undefine _missing_build_ids_terminate_build

Name:           grub2
Epoch:          1
Version:        2.00
Release:        18%{?dist}
Summary:        Bootloader with support for Linux, Multiboot and more

Group:          System Environment/Base
License:        GPLv3+
URL:            http://www.gnu.org/software/grub/
Obsoletes:	grub < 1:0.98
Source0:        ftp://alpha.gnu.org/gnu/grub/grub-%{tarversion}.tar.xz
Source3:        README.Fedora
Source4:	http://unifoundry.com/unifont-5.1.20080820.pcf.gz
Source5:	theme.tar.bz2
#Source6:	grub-cd.cfg
Patch0001: 0001-Add-monochrome-text-support-mda_text-aka-hercules-in.patch
Patch0002: 0002-missing-file-from-last-commit.patch
Patch0003: 0003-grub-core-loader-i386-linux.c-find_efi_mmap_size-Don.patch
Patch0004: 0004-include-grub-list.h-FOR_LIST_ELEMENTS_SAFE-New-macro.patch
Patch0005: 0005-gentpl.py-Make-mans-depend-on-grub-mkconfig_lib.patch
Patch0006: 0006-grub-core-net-tftp.c-ack-Fix-endianness-problem.patch
Patch0007: 0007-grub-core-fs-ext2.c-Experimental-support-for-64-bit.patch
Patch0008: 0008-grub-core-term-efi-serial.c-Support-1.5-stop-bits.patch
Patch0009: 0009-grub-core-lib-legacy_parse.c-Support-clear-and-testl.patch
Patch0010: 0010-grub-core-Makefile.am-Fix-path-to-boot-i386-pc-start.patch
Patch0011: 0011-Fix-coreboot-compilation.patch
Patch0012: 0012-grub-core-normal-autofs.c-autoload_fs_module-Save-an.patch
Patch0013: 0013-grub-core-lib-xzembed-xz_dec_stream.c-hash_validate-.patch
Patch0014: 0014-grub-core-loader-i386-bsd.c-grub_bsd_elf32_size_hook.patch
Patch0015: 0015-New-command-lsefi.patch
Patch0016: 0016-util-grub-mkconfig_lib.in-grub_quote-Remove-extra-la.patch
Patch0017: 0017-EHCI-and-OHCI-PCI-bus-master.patch
Patch0018: 0018-Update-manual-NetBSD-wise.patch
Patch0019: 0019-Regenerate-po-POTFILES.in-with-the-following-commman.patch
Patch0020: 0020-Strengthen-the-configure-test-for-working-nostdinc-i.patch
Patch0021: 0021-.bzrignore-Add-grub-bios-setup-grub-ofpathname-and.patch
Patch0022: 0022-docs-man-grub-mkdevicemap.h2m-Remove-since-grub-mkde.patch
Patch0023: 0023-grub-core-mmap-mips-loongson-Remove-empty-directory.patch
Patch0024: 0024-Makefile.am-EXTRA_DIST-Add.patch
Patch0025: 0025-Makefile.am-EXTRA_DIST-Add-linguas.sh.-It-s-only-str.patch
Patch0026: 0026-grub-core-fs-xfs.c-grub_xfs_read_block-Make-keys-a-c.patch
Patch0027: 0027-grub-core-partmap-dvh.c-grub_dvh_is_valid-Add-missin.patch
Patch0028: 0028-grub-core-script-yylex.l-Ignore-unused-function-and-.patch
Patch0029: 0029-grub-core-disk-ieee1275-ofdisk.c-scan-Check-function.patch
Patch0030: 0030-util-import_gcry.py-Sort-cipher_files-to-make-build-.patch
Patch0031: 0031-NEWS-Fix-typo.patch
Patch0032: 0032-configure.ac-Add-SuSe-path.patch
Patch0033: 0033-grub-core-Makefile.core.def-efifwsetup-New-module.patch
Patch0034: 0034-grub-core-loader-efi-appleloader.c-devpath_8-New-var.patch
Patch0035: 0035-grub-core-disk-diskfilter.c-free_array-GRUB_UTIL-Fix.patch
Patch0036: 0036-Don-t-require-grub-mkconfig_lib-to-generate-manpages.patch
Patch0037: 0037-include-grub-efi-api.h-grub_efi_runtime_services-Mak.patch
Patch0038: 0038-grub-core-term-terminfo.c-Only-fix-up-powerpc-key-re.patch
Patch0039: 0039-util-grub-mkconfig_lib.in-grub_quote-Remove-outdated.patch
Patch0040: 0040-grub-core-loader-i386-linux.c-grub_cmd_linux-Fix-inc.patch
Patch0041: 0041-grub-core-kern-ieee1275-cmain.c-grub_ieee1275_find_o.patch
Patch0042: 0042-util-grub-mkconfig_lib.in-grub_tab-New-variable.patch
Patch0043: 0043-util-grub-setup.c-write_rootdev-Remove-unused-core_i.patch
Patch0044: 0044-grub-core-partmap-msdos.c-pc_partition_map_embed-Rev.patch
Patch0045: 0045-Fix-grub-emu-build-on-FreeBSD.patch
Patch0046: 0046-util-grub-install.in-Make-the-error-message-if-sourc.patch
Patch0047: 0047-grub-core-fs-affs.c-grub_affs_mount-Support-AFFS-boo.patch
Patch0048: 0048-util-grub-mkconfig_lib.in-is_path_readable_by_grub-R.patch
Patch0049: 0049-Makefile.util.def-grub-mknetdir-Move-to-prefix-bin.patch
Patch0050: 0050-grub-core-loader-i386-linux.c-allocate_pages-Fix-spe.patch
Patch0051: 0051-grub-core-Makefile.am-moddep.lst-Use-AWK-instead-of-.patch
Patch0052: 0052-grub-core-commands-configfile.c-GRUB_MOD_INIT-Correc.patch
Patch0053: 0053-Fix-ordering-and-tab-indentation-of-NetBSD-boot-menu.patch
Patch0054: 0054-grub-core-net-bootp.c-parse_dhcp_vendor-Fix-double-i.patch
Patch0055: 0055-include-grub-types.h-Fix-functionality-unaffecting-t.patch
Patch0056: 0056-Support-big-endian-UFS1.patch
Patch0057: 0057-Fix-big-endian-mtime.patch
Patch0058: 0058-grub-core-fs-ufs.c-grub_ufs_dir-Stop-if-direntlen-is.patch
Patch0059: 0059-util-getroot.c-convert_system_partition_to_system_di.patch
Patch0060: 0060-util-grub-mkfont.c-argp_parser-Fix-a-typo-which-prev.patch
Patch0061: 0061-grub-core-term-gfxterm.c-grub_virtual_screen_setup-G.patch
Patch0062: 0062-grub-core-gfxmenu-view.c-init_terminal-Avoid-making-.patch
Patch0063: 0063-grub-core-kern-ieee1275-init.c-grub_machine_get_boot.patch
Patch0064: 0064-util-grub-install.in-Remove-stale-TODO.patch
Patch0065: 0065-util-grub-install.in-Follow-the-symbolic-link-parame.patch
Patch0066: 0066-grub-core-disk-cryptodisk.c-grub_cmd_cryptomount-Str.patch
Patch0067: 0067-docs-grub.texi-Network-Update-instructions-on-genera.patch
Patch0068: 0068-util-grub.d-20_linux_xen.in-Addmissing-assignment-to.patch
Patch0069: 0069-Backport-gnulib-fixes-for-C11.-Fixes-Savannah-bug-37.patch
Patch0070: 0070-Apply-program-name-transformations-at-build-time-rat.patch
Patch0071: 0071-neater-gnulib-backport.patch
Patch0072: 0072-util-grub-mkconfig.in-Accept-GRUB_TERMINAL_OUTPUT-vg.patch
Patch0073: 0073-grub-core-bus-usb-ehci.c-grub_ehci_pci_iter-Remove-i.patch
Patch0074: 0074-Remove-several-trivially-unnecessary-uses-of-nested-.patch
Patch0075: 0075-docs-grub.texi-configfile-Explain-environment-variab.patch
Patch0076: 0076-Fix-failing-printf-test.patch
Patch0077: 0077-grub-core-tests-lib-test.c-grub_test_run-Return-non-.patch
Patch0078: 0078-docs-grub.texi-Invoking-grub-mount-New-section.patch
Patch0079: 0079-docs-grub.texi-Invoking-grub-mkrelpath-New-section.patch
Patch0080: 0080-grub-core-fs-iso9660.c-grub_iso9660_susp_iterate-Avo.patch
Patch0081: 0081-configure.ac-Extend-Wno-trampolines-to-host.patch
Patch0082: 0082-util-grub.d-10_kfreebsd.in-Fix-improper-references-t.patch
Patch0083: 0083-util-grub.d-10_kfreebsd.in-Correct-the-patch-to-zpoo.patch
Patch0084: 0084-grub-core-disk-diskfilter.c-grub_diskfilter_write-Ca.patch
Patch0085: 0085-grub-core-fs-nilfs2.c-grub_nilfs2_palloc_groups_per_.patch
Patch0086: 0086-grub-core-fs-ntfs.c-Eliminate-useless-divisions-in-f.patch
Patch0087: 0087-grub-core-fs-ext2.c-grub_ext2_read_block-Use-shifts-.patch
Patch0088: 0088-grub-core-fs-minix.c-grub_minix_read_file-Simplify-a.patch
Patch0089: 0089-docs-grub.texi-grub_cpu-New-subsection.patch
Patch0090: 0090-grub-core-io-bufio.c-grub_bufio_open-Use-grub_zalloc.patch
Patch0091: 0091-grub-core-kern-disk.c-grub_disk_write-Fix-sector-num.patch
Patch0092: 0092-Support-Apple-FAT-binaries-on-non-Apple-platforms.patch
Patch0093: 0093-grub-core-fs-ntfs.c-Ue-more-appropriate-types.patch
Patch0094: 0094-Import-gcrypt-public-key-cryptography-and-implement-.patch
Patch0095: 0095-Clean-up-dangling-references-to-grub-setup.patch
Patch0096: 0096-autogen.sh-Do-not-try-to-delete-nonexistant-files.patch
Patch0097: 0097-Remove-autogenerated-files-from-VCS.patch
Patch0098: 0098-grub-core-lib-libgcrypt_wrap-mem.c-_gcry_log_bug-Mak.patch
Patch0099: 0099-grub-core-lib-libgcrypt_wrap-mem.c-gcry_x-alloc-Make.patch
Patch0100: 0100-grub-core-commands-verify.c-Mark-messages-for-transl.patch
Patch0101: 0101-Remove-nested-functions-from-PCI-iterators.patch
Patch0102: 0102-util-grub-mkimage.c-generate_image-Fix-size-of-publi.patch
Patch0103: 0103-New-command-list_trusted.patch
Patch0104: 0104-Fix-compilation-with-older-compilers.patch
Patch0105: 0105-grub-core-kern-emu-hostdisk.c-read_device_map-Explic.patch
Patch0106: 0106-Remove-nested-functions-from-memory-map-iterators.patch
Patch0107: 0107-Remove-nested-functions-from-script-reading-and-pars.patch
Patch0108: 0108-grub-core-script-lexer.c-grub_script_lexer_init-Rena.patch
Patch0109: 0109-Improve-bidi-handling-in-entry-editor.patch
Patch0110: 0110-New-terminal-outputs-using-serial-morse-and-spkmodem.patch
Patch0111: 0111-Add-new-command-pcidump.patch
Patch0112: 0112-Rewrite-spkmodem-to-use-PIT-for-timing.-Double-the-s.patch
Patch0113: 0113-Add-license-header-to-spkmodem-recv.c.patch
Patch0114: 0114-Fix-typos-for-developer-and-development.patch
Patch0115: 0115-Remove-nested-functions-from-device-iterators.patch
Patch0116: 0116-Remove-nested-functions-from-ELF-iterators.patch
Patch0117: 0117-util-grub-script-check.c-main-Uniform-the-error-mess.patch
Patch0118: 0118-docs-grub.texi-Simple-configuration-Clarify-GRUB_HID.patch
Patch0119: 0119-Split-long-USB-transfers-into-short-ones.patch
Patch0120: 0120-include-grub-elf.h-Update-ARM-definitions-based-on-b.patch
Patch0121: 0121-conf-Makefile.common-Fix-autogen-rules-to-pass-defin.patch
Patch0122: 0122-grub-core-loader-i386-linux.c-grub_cmd_initrd-Don-t-.patch
Patch0123: 0123-util-grub-mkimage.c-main-Postpone-freeing-arguments..patch
Patch0124: 0124-docs-grub.texi-Multi-boot-manual-config-Fix-typo-for.patch
Patch0125: 0125-Remove-nested-functions-from-filesystem-directory-it.patch
Patch0126: 0126-grub-core-partmap-msdos.c-embed_signatures-Add-the-s.patch
Patch0127: 0127-Improve-spkmomdem-reliability-by-adding-a-separator-.patch
Patch0128: 0128-grub-core-commands-lsmmap.c-Fix-unused-variable-on-e.patch
Patch0129: 0129-grub-core-disk-arc-arcdisk.c-grub_arcdisk_iterate-Fi.patch
Patch0130: 0130-Fix-powerpc-and-sparc64-build-failures-caused-by-un-.patch
Patch0131: 0131-grub-core-commands-ls.c-grub_ls_print_devices-Add-mi.patch
Patch0132: 0132-Make-color-variables-global-instead-of-it-being-per-.patch
Patch0133: 0133-Improve-spkmomdem-reliability-by-adding-a-separator-.patch
Patch0134: 0134-grub-core-normal-term.c-print_ucs4_terminal-Don-t-ou.patch
Patch0135: 0135-Improve-spkmodem-reliability-by-adding-a-separator-b.patch
Patch0136: 0136-Remove-nested-functions-from-USB-iterators.patch
Patch0137: 0137-grub-core-font-font.c-blit_comb-do_blit-Make-static-.patch
Patch0138: 0138-include-grub-kernel.h-FOR_MODULES-Adjust-to-preserve.patch
Patch0139: 0139-grub-core-lib-libgcrypt_wrap-cipher_wrap.h-Include-s.patch
Patch0140: 0140-util-grub-reboot.in-usage-Document-the-need-for.patch
Patch0141: 0141-Improve-FreeDOS-direct-loading-support-compatibility.patch
Patch0142: 0142-grub-core-normal-menu_text.c-grub_menu_init_page-Fix.patch
Patch0143: 0143-util-grub-install.in-change-misleading-comment-about.patch
Patch0144: 0144-grub-core-fs-xfs.c-grub_xfs_read_block-Fix-computati.patch
Patch0145: 0145-grub-core-bus-usb-serial-common.c-grub_usbserial_att.patch
Patch0146: 0146-grub-core-bus-usb-usb.c-grub_usb_device_attach-Add-m.patch
Patch0147: 0147-grub-core-commands-lsacpi.c-Show-more-info.-Hide-som.patch
Patch0148: 0148-Missing-part-of-last-commit.patch
Patch0149: 0149-Implement-USBDebug-full-USB-stack-variant.patch
Patch0150: 0150-grub-core-fs-fshelp.c-find_file-Set-oldnode-to-zero-.patch
Patch0151: 0151-grub-core-disk-cryptodisk.c-grub_cryptodisk_scan_dev.patch
Patch0152: 0152-grub-core-commands-lsacpi.c-Fix-types-on-64-bit-plat.patch
Patch0153: 0153-Support-Openfirmware-disks-with-non-512B-sectors.patch
Patch0154: 0154-Implement-new-command-cmosdump.patch
Patch0155: 0155-grub-core-normal-misc.c-grub_normal_print_device_inf.patch
Patch0156: 0156-Makefile.util.def-Add-partmap-msdos.c-to-common-libr.patch
Patch0157: 0157-grub-core-normal-menu_entry.c-insert_string-fix-off-.patch
Patch0158: 0158-grub-core-normal-menu_entry.c-update_screen-remove.patch
Patch0159: 0159-grub-core-disk-efi-efidisk.c-grub_efidisk_get_device.patch
Patch0160: 0160-grub-core-partmap-msdos.c-grub_partition_msdos_itera.patch
Patch0161: 0161-Remove-nested-functions-from-disk-and-file-read-hook.patch
Patch0162: 0162-grub-core-loader-machoXX.c-Remove-nested-functions.patch
Patch0163: 0163-util-grub-fstest.c-Remove-nested-functions.patch
Patch0164: 0164-grub-core-commands-parttool.c-grub_cmd_parttool-Move.patch
Patch0165: 0165-grub-core-fs-iso9660.c-Remove-nested-functions.patch
Patch0166: 0166-grub-core-fs-minix.c-Remove-nested-functions.patch
Patch0167: 0167-grub-core-fs-jfs.c-Remove-nested-functions.patch
Patch0168: 0168-grub-core-lib-arg.c-grub_arg_show_help-Move-showargs.patch
Patch0169: 0169-grub-core-kern-i386-coreboot-mmap.c-grub_linuxbios_t.patch
Patch0170: 0170-Enable-linux16-on-non-BIOS-systems-for-i.a.-memtest.patch
Patch0171: 0171-grub-core-kern-main.c-grub_set_prefix_and_root-Strip.patch
Patch0172: 0172-grub-core-disk-efi-efidisk.c-Transform-iterate_child.patch
Patch0173: 0173-grub-core-loader-i386-pc-linux.c-grub_cmd_linux-Fix-.patch
Patch0174: 0174-Remove-nested-functions-from-videoinfo-iterators.patch
Patch0175: 0175-grub-core-gentrigtables.c-Make-tables-const.patch
Patch0176: 0176-grub-core-kern-emu-hostdisk.c-read_device_map-Remove.patch
Patch0177: 0177-util-grub-editenv.c-list_variables-Move-print_var-ou.patch
Patch0178: 0178-grub-core-fs-hfsplus.c-grub_hfsplus_btree_iterate_no.patch
Patch0179: 0179-grub-core-fs-hfs.c-Remove-nested-functions.patch
Patch0180: 0180-grub-core-commands-loadenv.c-grub_cmd_list_env-Move-.patch
Patch0181: 0181-grub-core-normal-charset.c-grub_bidi_logical_to_visu.patch
Patch0182: 0182-grub-core-script-execute.c-gettext_append-Remove-nes.patch
Patch0183: 0183-grub-core-lib-ia64-longjmp.S-Fix-the-name-of-longjmp.patch
Patch0184: 0184-Make-elfload-not-use-hooks.-Opt-for-flags-and-iterat.patch
Patch0185: 0185-grub-core-kern-term.c-grub_term_normal_color.patch
Patch0186: 0186-Move-to-more-hookless-approach-in-IEEE1275-devices-h.patch
Patch0187: 0187-include-grub-mips-loongson-cmos.h-Fix-high-CMOS-addr.patch
Patch0188: 0188-include-grub-cmos.h-Handle-high-CMOS-addresses-on-sp.patch
Patch0189: 0189-grub-core-disk-ieee1275-nand.c-Fix-compilation-on.patch
Patch0190: 0190-grub-core-kern-env.c-include-grub-env.h-Change-itera.patch
Patch0191: 0191-grub-core-commands-regexp.c-set_matches-Move-setvar-.patch
Patch0192: 0192-grub-core-script-execute.c-grub_script_arglist_to_ar.patch
Patch0193: 0193-Remove-all-trampoline-support.-Add-Wtrampolines-when.patch
Patch0194: 0194-grub-core-term-terminfo.c-grub_terminfo_cls-Issue-an.patch
Patch0195: 0195-Lift-up-core-size-limits-on-some-platforms.-Fix-pote.patch
Patch0196: 0196-grub-core-normal-crypto.c-read_crypto_list-Fix-incor.patch
Patch0197: 0197-grub-core-commands-acpi.c-grub_acpi_create_ebda-Don-.patch
Patch0198: 0198-grub-core-fs-iso9660.c-add_part-Remove-always_inline.patch
Patch0199: 0199-grub-core-fs-fshelp.c-grub_fshelp_log2blksize-Remove.patch
Patch0200: 0200-Avoid-costly-64-bit-division-in-grub_get_time_ms-on-.patch
Patch0201: 0201-grub-core-fs-hfs.c-grub_hfs_read_file-Avoid-divmod64.patch
Patch0202: 0202-Adjust-types-in-gdb-module-to-have-intended-unsigned.patch
Patch0203: 0203-grub-core-video-i386-pc-vbe.c.patch
Patch0204: 0204-include-grub-datetime.h-grub_datetime2unixtime-Fix-u.patch
Patch0205: 0205-grub-core-loader-i386-pc-plan9.c-fill_disk-Fix-types.patch
Patch0206: 0206-grub-core-commands-verify.c-grub_verify_signature-Us.patch
Patch0207: 0207-grub-core-lib-arg.c-grub_arg_list_alloc-Use-shifts-r.patch
Patch0208: 0208-grub-core-loader-i386-bsdXX.c-grub_openbsd_find_ramd.patch
Patch0209: 0209-Resend-a-packet-if-we-got-the-wrong-buffer-in-status.patch
Patch0210: 0210-Better-estimate-the-maximum-USB-transfer-size.patch
Patch0211: 0211-remove-get_endpoint_descriptor-and-change-all-functi.patch
Patch0212: 0212-Implement-boot-time-analysis-framework.patch
Patch0213: 0213-Fix-USB-devices-not-being-detected-when-requested.patch
Patch0214: 0214-Initialize-USB-ports-in-parallel-to-speed-up-boot.patch
Patch0215: 0215-include-grub-boottime.h-Add-missing-file.patch
Patch0216: 0216-Fix-a-conflict-between-ports-structures-with-2-contr.patch
Patch0217: 0217-New-commands-cbmemc-lscoreboot-coreboot_boottime-to-.patch
Patch0218: 0218-grub-core-commands-boottime.c-Fix-copyright-header.patch
Patch0219: 0219-Slight-improve-in-USB-related-boot-time-checkpoints.patch
Patch0220: 0220-grub-core-commands-verify.c-hashes-Add-several-hashe.patch
Patch0221: 0221-po-POTFILES.in-Regenerate.patch
Patch0222: 0222-grub-core-commands-i386-coreboot-cbls.c-Fix-typos-an.patch
Patch0223: 0223-Add-ability-to-generate-newc-additions-on-runtime.patch
Patch0224: 0224-grub-core-fs-zfs-zfs.c-Fix-incorrect-handling-of-spe.patch
Patch0225: 0225-grub-core-term-at_keyboard.c-Increase-robustness-on-.patch
Patch0226: 0226-Add-new-proc-filesystem-framework-and-put-luks_scrip.patch
Patch0227: 0227-grub-core-Makefile.core.def-vbe-Disable-on-coreboot-.patch
Patch0228: 0228-util-grub-mkconfig_lib.in-prepare_grub_to_access_dev.patch
Patch0229: 0229-grub-core-Makefile.core.def-vga-Disable-on-coreboot-.patch
Patch0230: 0230-util-grub.d-20_linux_xen.in-Automatically-add-no-rea.patch
Patch0231: 0231-Replace-the-region-at-0-from-coreboot-tables-to-avai.patch
Patch0232: 0232-grub-core-normal-menu.c-Wait-if-there-were-errors-sh.patch
Patch0233: 0233-grub-core-disk-ahci.c-Give-more-time-for-AHCI-reques.patch
Patch0234: 0234-grub-core-gfxmenu-font.c-grub_font_get_string_width-.patch
Patch0235: 0235-grub-core-commands-acpihalt.c-skip_ext_op-Add-suppor.patch
Patch0236: 0236-grub-core-kern-efi-mm.c-grub_efi_finish_boot_service.patch
Patch0237: 0237-grub-core-commands-verify.c-Fix-hash-algorithms-valu.patch
Patch0238: 0238-INSTALL-Mention-xorriso-requirement.patch
Patch0239: 0239-grub-core-partmap-apple.c-apple_partition_map_iterat.patch
Patch0240: 0240-grub-core-gfxmenu-gui_circular_progress.c-Fix-off-by.patch
Patch0241: 0241-grub-core-gfxmenu-view.c-Fix-off-by-one-error.patch
Patch0242: 0242-grub-core-gfxmenu-gui_circular_progress.c-Take-both-.patch
Patch0243: 0243-grub-core-gfxmenu-gui_progress_bar.c-Handle-padding-.patch
Patch0244: 0244-include-grub-elf.h-Add-missing-ARM-relocation-codes-.patch
Patch0245: 0245-util-grub-mount.c-fuse_init-Return-error-if-fuse_mai.patch
Patch0246: 0246-Fix-screen-corruption-in-menu-entry-editor-and-simpl.patch
Patch0247: 0247-grub-core-term-i386-pc-console.c-grub_console_getwh-.patch
Patch0248: 0248-grub-core-commands-verify.c-Save-verified-file-to-av.patch
Patch0249: 0249-grub-core-lib-posix_wrap-locale.h-GRUB_UTIL-Include-.patch
Patch0250: 0250-util-grub-setup.c-setup-Handle-some-corner-cases.patch
Patch0251: 0251-grub-core-bus-usb-usbtrans.c-grub_usb_bulk_readwrite.patch
Patch0252: 0252-Use-TSC-as-a-possible-time-source-on-i386-ieee1275.patch
Patch0253: 0253-grub-core-disk-efi-efidisk.c-Handle-partitions-on-no.patch
Patch0254: 0254-Unify-file-copying-setup-across-different-install-sc.patch
Patch0255: 0255-util-grub-mkimage.c-Introduce-new-define-EFI32_HEADE.patch
Patch0256: 0256-docs-grub.texi-Document-menuentry-id-option.patch
Patch0257: 0257-docs-grub.texi-Document-more-user-commands.patch
Patch0258: 0258-Move-GRUB_CHAR_BIT-to-types.h.patch
Patch0259: 0259-include-grub-bsdlabel.h-Use-enums.patch
Patch0260: 0260-grub-core-commands-verify.c-Use-GRUB_CHAR_BIT.patch
Patch0261: 0261-Add-new-defines-GRUB_RSDP_SIGNATURE_SIZE-and-GRUB_RS.patch
Patch0262: 0262-Replace-8-with-GRUB_CHAR_BIT-in-several-places-when-.patch
Patch0263: 0263-grub-core-commands-acpi.c-Use-sizeof-rather-than-har.patch
Patch0264: 0264-util-grub-mkfont.c-Prefer-enum-to-define.patch
Patch0265: 0265-Use-GRUB_PROPERLY_ALIGNED_ARRAY-in-grub-core-disk-cr.patch
Patch0266: 0266-util-grub.d-30_os-prober.in-Support-btrrfs-linux-pro.patch
Patch0267: 0267-util-grub-install_header-Use-PACKAGE-.mo-in-message-.patch
Patch0268: 0268-conf-Makefile.extra-dist-EXTRA_DIST-Add.patch
Patch0269: 0269-grub-core-normal-term.c-Few-more-fixes-for-menu-entr.patch
Patch0270: 0270-grub-core-normal-term.c-Few-more-fixes-for-menu-entr.patch
Patch0271: 0271-docs-grub-dev.texi-Move-itemize-after-subsection-to-.patch
Patch0272: 0272-grub-core-term-i386-pc-console.c-Fix-cursor-moving-a.patch
Patch0273: 0273-grub-core-Makefile.core.def-Add-kern-elfXX.c-to-elf-.patch
Patch0274: 0274-Fix-ia64-efi-image-generation-on-big-endian-machines.patch
Patch0275: 0275-autogen.sh-Use-h-not-f-to-test-for-existence-of-symb.patch
Patch0276: 0276-Fix-missing-PVs-if-they-don-t-contain-interesting-LV.patch
Patch0277: 0277-util-grub.d-30_os-prober.in-Add-onstr-to-entries-for.patch
Patch0278: 0278-Use-ACPI-shutdown-intests-as-traditional-port-was-re.patch
Patch0279: 0279-Import-new-gnulib.patch
Patch0280: 0280-docs-grub.texi-Fix-description-of-GRUB_CMDLINE_XEN-a.patch
Patch0281: 0281-Merge-powerpc-grub-mkrescue-flavour-with-common.-Use.patch
Patch0282: 0282-Support-i386-ieee1275-grub-mkrescue-and-make-check-o.patch
Patch0283: 0283-tests-partmap_test.in-Fix-missing-qemudisk-setting.patch
Patch0284: 0284-tests-grub_cmd_date.in-New-test-for-datetime.patch
Patch0285: 0285-docs-grub.texi-Update-coreboot-status-info.patch
Patch0286: 0286-Turn-off-QEMU-ACPI-way-since-new-releases-don-t-have.patch
Patch0287: 0287-tests-util-grub-shell.in-Fix-it-on-powerpc.patch
Patch0288: 0288-Disable-partmap-check-on-i386-ieee1275-due-to-openfi.patch
Patch0289: 0289-grub-core-net-drivers-ieee1275-ofnet.c-Don-t-attempt.patch
Patch0290: 0290-grub-core-net-http.c-Fix-bad-free.patch
Patch0291: 0291-Fix-handling-of-split-transfers.patch
Patch0292: 0292-grub-core-bus-usb-ehci.c-grub_ehci_fini_hw-Ignore-er.patch
Patch0293: 0293-util-grub-mkimage.c-Document-memdisk-implying-prefix.patch
Patch0294: 0294-Handle-Japanese-special-keys.patch
Patch0295: 0295-Replace-stpcpy-with-grub_stpcpy-in-tools.patch
Patch0296: 0296-Better-support-Apple-Intel-Macs-on-CD.patch
Patch0297: 0297-util-grub-mkrescue.in-Fix-wrong-architecture-for-ppc.patch
Patch0298: 0298-docs-man-grub-glue-efi.h2m-Add-missing-file.patch
Patch0299: 0299-Fix-memory-leaks-in-ofnet.patch
Patch0300: 0300-grub-core-kern-ieee1275-cmain.c-grub_ieee1275_find_o.patch
Patch0301: 0301-grub-core-disk-ieee1275-ofdisk.c-Iterate-over-bootpa.patch
Patch0302: 0302-Allow-IEEE1275-ports-on-path-even-if-it-wasn-t-detec.patch
Patch0303: 0303-Support-mkrescue-on-sparc64.patch
Patch0304: 0304-Support-grub-shell-on-sparc64.patch
Patch0305: 0305-tests-partmap_test.in-Skip-on-sparc64.patch
Patch0306: 0306-tests-grub_cmd_date.in-Add-missing-exit-1.patch
Patch0307: 0307-Move-GRUB-out-of-system-area-when-using-xorriso-1.2..patch
Patch0308: 0308-grub-core-loader-i386-linux.c-Remove-useless-leftove.patch
Patch0309: 0309-docs-grub-dev.texi-Rearrange-menu-to-match-the-secti.patch
Patch0310: 0310-Add-option-to-compress-files-on-install-image-creati.patch
Patch0311: 0311-grub-core-lib-posix_wrap-sys-types.h-Make-WORDS_BIGE.patch
Patch0312: 0312-grub-core-disk-ieee1275-ofdisk.c-Fix-CD-ROM-and-boot.patch
Patch0313: 0313-grub-core-kern-ieee1275-openfw.c-grub_ieee1275_deval.patch
Patch0314: 0314-tests-grub_script_expansion.in-Use-fixed-string-grep.patch
Patch0315: 0315-tests-grub_cmd_date.in-Skip-on-sparc64.patch
Patch0316: 0316-Fix-DMRAID-partition-handling.patch
Patch0317: 0317-grub-core-disk-efi-efidisk.c-Limit-disk-read-or-writ.patch
Patch0318: 0318-autogen.sh-Use-f-in-addition-for-h-when-checking-fil.patch
Patch0319: 0319-grub-core-disk-efi-efidisk.c-Really-limit-transfer-c.patch
Patch0320: 0320-build-aux-snippet-Add-missing-gnulib-files.patch
Patch0321: 0321-grub-core-disk-efi-efidisk.c-Detect-floppies-by-ACPI.patch
Patch0322: 0322-util-grub-mkrescue.in-Add-GPT-for-EFI-boot.patch
Patch0323: 0323-Add-support-for-pseries-and-other-bootinfo-machines-.patch
Patch0324: 0324-util-grub.d-30_os-prober.in-Add-onstr-to-linux-entri.patch
Patch0325: 0325-grub-core-kern-elfXX.c-grub_elfXX_load-Handle.patch
Patch0326: 0326-grub-core-commands-videotest.c-grub_cmd_videotest-Fi.patch
Patch0327: 0327-grub-core-kern-ieee1275-cmain.c-grub_ieee1275_find_o.patch
Patch0328: 0328-grub-core-kern-ieee1275-init.c-grub_claim_heap-Impro.patch
Patch0329: 0329-grub-core-lib-efi-relocator.c-grub_relocator_firmwar.patch
Patch0330: 0330-grub-core-Makefile.core.def-legacycfg-Enable-on-EFI.patch
Patch0331: 0331-grub-core-kern-mm.c-grub_mm_init_region-Fix-conditio.patch
Patch0332: 0332-Support-coreboot-framebuffer.patch
Patch0333: 0333-grub-core-disk-arc-arcdisk.c-grub_arcdisk_iterate_it.patch
Patch0334: 0334-Move-mips-arc-link-address.-Previous-link-address-wa.patch
Patch0335: 0335-grub-core-kern-dl.c-grub_dl_resolve_symbols-Handle-m.patch
Patch0336: 0336-util-grub-mkrescue.in-Add-mips-arc-support.patch
Patch0337: 0337-Add-missing-video-ids-to-coreboot-and-ieee1275-video.patch
Patch0338: 0338-grub-core-disk-ata.c-grub_ata_real_open-Use-grub_err.patch
Patch0339: 0339-grub-core-loader-i386-linux.c-grub_linux_boot-Defaul.patch
Patch0340: 0340-grub-core-normal-menu_text.c-print_entry-Put-an-aste.patch
Patch0341: 0341-util-grub-install.in-Fix-target-fo-qemu_mips.patch
Patch0342: 0342-Don-t-say-GNU-Linux-in-generated-menus.patch
Patch0343: 0343-Migrate-PPC-from-Yaboot-to-Grub2.patch
Patch0344: 0344-Add-fw_path-variable-revised.patch
Patch0345: 0345-Don-t-set-boot-device-on-ppc-ieee1275.patch
Patch0346: 0346-Add-support-for-linuxefi.patch
Patch0347: 0347-Add-support-for-crappy-cd-craparino.patch
Patch0348: 0348-Use-linuxefi-and-initrdefi-where-appropriate.patch
Patch0349: 0349-Don-t-allow-insmod-when-secure-boot-is-enabled.patch
Patch0351: 0351-Pass-x-hex-hex-straight-through-unmolested.patch
Patch0352: 0352-Fix-crash-on-http.patch
Patch0353: 0353-Issue-separate-DNS-queries-for-ipv4-and-ipv6.patch
Patch0354: 0354-IBM-client-architecture-CAS-reboot-support.patch
Patch0355: 0355-for-ppc-include-all-modules-in-the-core-image.patch
Patch0356: 0356-Add-vlan-tag-support.patch
Patch0357: 0357-Add-X-option-to-printf-functions.patch
Patch0358: 0358-DHCP-client-ID-and-UUID-options-added.patch
Patch0359: 0359-Search-for-specific-config-file-for-netboot.patch
Patch0360: 0360-Add-bootpath-device-to-the-list.patch
Patch0361: 0361-add-GRUB_DISABLE_SUBMENU-option.patch
Patch0362: 0362-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch0363: 0363-Move-bash-completion-script-922997.patch
Patch0364: 0002-configure.ac-Don-t-use-extended-registers-on-x86_64.patch
Patch0365: 0003-configure.ac-Don-t-disable-extended-registers-on-emu.patch
Patch0366: 0004-conf-Makefile.common-Poison-float-and-double-on-non-.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  flex bison binutils python
BuildRequires:  ncurses-devel xz-devel
BuildRequires:  freetype-devel libusb-devel
%ifarch %{sparc} x86_64
# sparc builds need 64 bit glibc-devel - also for 32 bit userland
BuildRequires:  /usr/lib64/crt1.o glibc-static
%else
# ppc64 builds need the ppc crt1.o
BuildRequires:  /usr/lib/crt1.o glibc-static
%endif
BuildRequires:  autoconf automake autogen device-mapper-devel
BuildRequires:	freetype-devel gettext-devel git
BuildRequires:	texinfo
BuildRequires:	dejavu-sans-fonts
%ifarch %{efiarchs}
BuildRequires:	pesign >= 0.99-8
%endif

Requires:	gettext os-prober which file
Requires:	%{name}-tools = %{epoch}:%{version}-%{release}
Requires(pre):  dracut
Requires(post): dracut

ExcludeArch:	s390 s390x %{arm}

%description
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for PC BIOS systems.

%ifarch %{efiarchs}
%package efi
Summary:	GRUB for EFI systems.
Group:		System Environment/Base
Requires:	%{name}-tools = %{epoch}:%{version}-%{release}

%description efi
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides support for EFI systems.
%endif

%package tools
Summary:	Support tools for GRUB.
Group:		System Environment/Base
Requires:	gettext os-prober which file system-logos

%description tools
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides tools for support of all platforms.

%package starfield-theme
Summary:	An example theme for GRUB.
Group:		System Environment/Base
Requires:	system-logos

%description starfield-theme
The GRand Unified Bootloader (GRUB) is a highly configurable and customizable
bootloader with modular architecture.  It support rich varietyof kernel formats,
file systems, computer architectures and hardware devices.  This subpackage
provides an example theme for the grub screen.

%prep
%setup -T -c -n grub-%{tarversion}
%ifarch %{efiarchs}
%setup -D -q -T -a 0 -n grub-%{tarversion}
cd grub-%{tarversion}
cp %{SOURCE3} .
# place unifont in the '.' from which configure is run
cp %{SOURCE4} unifont.pcf.gz
git init
git config user.email "grub2-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{tarversion} baseline."
git am %{patches}
cd ..
mv grub-%{tarversion} grub-efi-%{tarversion}
%endif
%setup -D -q -T -a 0 -n grub-%{tarversion}
cd grub-%{tarversion}
cp %{SOURCE3} .
# place unifont in the '.' from which configure is run
cp %{SOURCE4} unifont.pcf.gz
git init
git config user.email "grub2-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{tarversion} baseline."
git am %{patches}

%build
%ifarch %{efiarchs}
cd grub-efi-%{tarversion}
./autogen.sh
%configure							\
	CFLAGS="$(echo $RPM_OPT_FLAGS | sed			\
		-e 's/-O.//g'					\
		-e 's/-fstack-protector//g'			\
		-e 's/--param=ssp-buffer-size=4//g'		\
		-e 's/-mregparm=3/-mregparm=4/g'		\
		-e 's/-fexceptions//g'				\
		-e 's/-fasynchronous-unwind-tables//g' )"	\
	TARGET_LDFLAGS=-static					\
        --with-platform=efi					\
	--with-grubdir=%{name}					\
        --program-transform-name=s,grub,%{name},		\
	--disable-werror
make %{?_smp_mflags}
GRUB_MODULES="	all_video boot btrfs cat chain configfile echo efifwsetup \
		efinet ext2 fat font gfxmenu gfxterm gzio halt hfsplus iso9660 \
		jpeg linuxefi lvm minicmd normal part_apple part_msdos \
		part_gpt password_pbkdf2 png reboot search search_fs_uuid \
		search_fs_file search_label sleep test video xfs \
		mdraid09 mdraid1x blscfg"
./grub-mkimage -O %{grubefiarch} -o %{grubeficdname}.orig -p /EFI/BOOT \
		-d grub-core ${GRUB_MODULES}
%pesign -s -i %{grubeficdname}.orig -o %{grubeficdname}
./grub-mkimage -O %{grubefiarch} -o %{grubefiname}.orig -p /EFI/%{efidir} \
		-d grub-core ${GRUB_MODULES}
%pesign -s -i %{grubefiname}.orig -o %{grubefiname}
cd ..
%endif

cd grub-%{tarversion}
./autogen.sh
# -static is needed so that autoconf script is able to link
# test that looks for _start symbol on 64 bit platforms
%ifarch %{sparc} ppc ppc64
%define platform ieee1275
%else
%define platform pc
%endif
%configure							\
	CFLAGS="$(echo $RPM_OPT_FLAGS | sed			\
		-e 's/-O.//g'					\
		-e 's/-fstack-protector//g'			\
		-e 's/--param=ssp-buffer-size=4//g'		\
		-e 's/-mregparm=3/-mregparm=4/g'		\
		-e 's/-fexceptions//g'				\
		-e 's/-m64//g'					\
		-e 's/-fasynchronous-unwind-tables//g' )"	\
	TARGET_LDFLAGS=-static					\
        --with-platform=%{platform}				\
	--with-grubdir=%{name}					\
        --program-transform-name=s,grub,%{name},		\
	--disable-werror

make %{?_smp_mflags}

sed -i -e 's,(grub),(%{name}),g' \
	-e 's,grub.info,%{name}.info,g' \
	-e 's,\* GRUB:,* GRUB2:,g' \
	-e 's,/boot/grub/,/boot/%{name}/,g' \
	-e 's,\([^-]\)grub-\([a-z]\),\1%{name}-\2,g' \
	docs/grub.info
sed -i -e 's,grub-dev,%{name}-dev,g' docs/grub-dev.info

/usr/bin/makeinfo --html --no-split -I docs -o grub-dev.html docs/grub-dev.texi
/usr/bin/makeinfo --html --no-split -I docs -o grub.html docs/grub.texi
sed -i	-e 's,/boot/grub/,/boot/%{name}/,g' \
	-e 's,\([^-]\)grub-\([a-z]\),\1%{name}-\2,g' \
	grub.html

%install
set -e
rm -fr $RPM_BUILD_ROOT

%ifarch %{efiarchs}
cd grub-efi-%{tarversion}
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -iname "*.module" -exec chmod a-x {} \;

# Ghost config file
install -m 755 -d $RPM_BUILD_ROOT/boot/efi/EFI/%{efidir}/
touch $RPM_BUILD_ROOT/boot/efi/EFI/%{efidir}/grub.cfg
ln -s ../boot/efi/EFI/%{efidir}/grub.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}-efi.cfg

# Install ELF files modules and images were created from into
# the shadow root, where debuginfo generator will grab them from
find $RPM_BUILD_ROOT -name '*.mod' -o -name '*.img' |
while read MODULE
do
        BASE=$(echo $MODULE |sed -r "s,.*/([^/]*)\.(mod|img),\1,")
        # Symbols from .img files are in .exec files, while .mod
        # modules store symbols in .elf. This is just because we
        # have both boot.img and boot.mod ...
        EXT=$(echo $MODULE |grep -q '.mod' && echo '.elf' || echo '.exec')
        TGT=$(echo $MODULE |sed "s,$RPM_BUILD_ROOT,.debugroot,")
#        install -m 755 -D $BASE$EXT $TGT
done
install -m 755 %{grubefiname} $RPM_BUILD_ROOT/boot/efi/EFI/%{efidir}/%{grubefiname}
install -m 755 %{grubeficdname} $RPM_BUILD_ROOT/boot/efi/EFI/%{efidir}/%{grubeficdname}
install -D -m 644 unicode.pf2 $RPM_BUILD_ROOT/boot/efi/EFI/%{efidir}/fonts/unicode.pf2
cd ..
%endif

cd grub-%{tarversion}
make DESTDIR=$RPM_BUILD_ROOT install

# Ghost config file
install -d $RPM_BUILD_ROOT/boot/%{name}
touch $RPM_BUILD_ROOT/boot/%{name}/grub.cfg
ln -s ../boot/%{name}/grub.cfg $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.cfg

# Install ELF files modules and images were created from into
# the shadow root, where debuginfo generator will grab them from
find $RPM_BUILD_ROOT -name '*.mod' -o -name '*.img' |
while read MODULE
do
        BASE=$(echo $MODULE |sed -r "s,.*/([^/]*)\.(mod|img),\1,")
        # Symbols from .img files are in .exec files, while .mod
        # modules store symbols in .elf. This is just because we
        # have both boot.img and boot.mod ...
        EXT=$(echo $MODULE |grep -q '.mod' && echo '.elf' || echo '.exec')
        TGT=$(echo $MODULE |sed "s,$RPM_BUILD_ROOT,.debugroot,")
#        install -m 755 -D $BASE$EXT $TGT
done

mv $RPM_BUILD_ROOT%{_infodir}/grub.info $RPM_BUILD_ROOT%{_infodir}/%{name}.info
mv $RPM_BUILD_ROOT%{_infodir}/grub-dev.info $RPM_BUILD_ROOT%{_infodir}/%{name}-dev.info
rm $RPM_BUILD_ROOT%{_infodir}/dir

# Defaults
mkdir ${RPM_BUILD_ROOT}%{_sysconfdir}/default
touch ${RPM_BUILD_ROOT}%{_sysconfdir}/default/grub
mkdir ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
ln -sf %{_sysconfdir}/default/grub \
	${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/grub

cd ..
%find_lang grub

# Fedora theme in /boot/grub2/themes/system/
cd $RPM_BUILD_ROOT
tar xjf %{SOURCE5}
$RPM_BUILD_ROOT%{_bindir}/%{name}-mkfont -o boot/grub2/themes/system/DejaVuSans-10.pf2      -s 10 /usr/share/fonts/dejavu/DejaVuSans.ttf # "DejaVu Sans Regular 10"
$RPM_BUILD_ROOT%{_bindir}/%{name}-mkfont -o boot/grub2/themes/system/DejaVuSans-12.pf2      -s 12 /usr/share/fonts/dejavu/DejaVuSans.ttf # "DejaVu Sans Regular 12"
$RPM_BUILD_ROOT%{_bindir}/%{name}-mkfont -o boot/grub2/themes/system/DejaVuSans-Bold-14.pf2 -s 14 /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf # "DejaVu Sans Bold 14"

# Make selinux happy with exec stack binaries.
mkdir ${RPM_BUILD_ROOT}%{_sysconfdir}/prelink.conf.d/
cat << EOF > ${RPM_BUILD_ROOT}%{_sysconfdir}/prelink.conf.d/grub2.conf
# these have execstack, and break under selinux
-b /usr/bin/grub2-script-check
-b /usr/bin/grub2-mkrelpath
-b /usr/bin/grub2-fstest
-b /usr/sbin/grub2-bios-setup
-b /usr/sbin/grub2-probe
-b /usr/sbin/grub2-sparc64-setup
EOF

%clean    
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
	/sbin/install-info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz || :
	/sbin/install-info --info-dir=%{_infodir} %{_infodir}/%{name}-dev.info.gz || :
fi

%triggerun -- grub2 < 1:1.99-4
# grub2 < 1.99-4 removed a number of essential files in postun. To fix upgrades
# from the affected grub2 packages, we first back up the files in triggerun and
# later restore them in triggerpostun.
# https://bugzilla.redhat.com/show_bug.cgi?id=735259

# Back up the files before uninstalling old grub2
mkdir -p /boot/grub2.tmp &&
mv -f /boot/grub2/*.mod \
      /boot/grub2/*.img \
      /boot/grub2/*.lst \
      /boot/grub2/device.map \
      /boot/grub2.tmp/ || :

%triggerpostun -- grub2 < 1:1.99-4
# ... and restore the files.
test ! -f /boot/grub2/device.map &&
test -d /boot/grub2.tmp &&
mv -f /boot/grub2.tmp/*.mod \
      /boot/grub2.tmp/*.img \
      /boot/grub2.tmp/*.lst \
      /boot/grub2.tmp/device.map \
      /boot/grub2/ &&
rm -r /boot/grub2.tmp/ || :

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz || :
	/sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/%{name}-dev.info.gz || :
fi

%files -f grub.lang
%defattr(-,root,root,-)
%{_libdir}/grub/*-%{platform}/
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%ghost %config(noreplace) /boot/%{name}/grub.cfg
%doc grub-%{tarversion}/COPYING

%ifarch %{efiarchs}
%files efi
%defattr(-,root,root,-)
%{_libdir}/grub/%{grubefiarch}
%config(noreplace) %{_sysconfdir}/%{name}-efi.cfg
%attr(0755,root,root)/boot/efi/EFI/%{efidir}
%attr(0755,root,root)/boot/efi/EFI/%{efidir}/fonts
%ghost %config(noreplace) /boot/efi/EFI/%{efidir}/grub.cfg
%doc grub-%{tarversion}/COPYING
%endif

%files tools -f grub.lang
%defattr(-,root,root,-)
%dir %{_libdir}/grub/
%dir %{_datarootdir}/grub/
%dir %{_datarootdir}/grub/themes
%{_datarootdir}/grub/*
%{_sbindir}/%{name}-mkconfig
%{_sbindir}/%{name}-install
%{_sbindir}/%{name}-probe
%{_sbindir}/%{name}-reboot
%{_sbindir}/%{name}-set-default
%{_sbindir}/%{name}-bios-setup
%{_sbindir}/%{name}-ofpathname
%{_sbindir}/%{name}-sparc64-setup
%{_bindir}/%{name}-mknetdir
%{_bindir}/%{name}-mkstandalone
%{_bindir}/%{name}-editenv
%{_bindir}/%{name}-fstest
%{_bindir}/%{name}-kbdcomp
%{_bindir}/%{name}-menulst2cfg
%{_bindir}/%{name}-mkfont
%{_bindir}/%{name}-mklayout
%{_bindir}/%{name}-mkimage
%{_bindir}/%{name}-mkpasswd-pbkdf2
%{_bindir}/%{name}-mkrelpath
%{_bindir}/%{name}-glue-efi
%{_bindir}/%{name}-render-label
%ifnarch %{sparc}
%{_bindir}/%{name}-mkrescue
%endif
%{_bindir}/%{name}-script-check
%{_datarootdir}/bash-completion/completions/grub
%{_sysconfdir}/prelink.conf.d/grub2.conf
%attr(0700,root,root) %dir %{_sysconfdir}/grub.d
%config %{_sysconfdir}/grub.d/??_*
%{_sysconfdir}/grub.d/README
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/default/grub
%{_sysconfdir}/sysconfig/grub
%dir /boot/%{name}
/boot/%{name}/themes/
%{_infodir}/%{name}*
%exclude %{_mandir}
%doc grub-%{tarversion}/COPYING grub-%{tarversion}/INSTALL
%doc grub-%{tarversion}/NEWS grub-%{tarversion}/README
%doc grub-%{tarversion}/THANKS grub-%{tarversion}/TODO
%doc grub-%{tarversion}/ChangeLog grub-%{tarversion}/README.Fedora
%doc grub-%{tarversion}/grub.html
%doc grub-%{tarversion}/grub-dev.html grub-%{tarversion}/docs/font_char_metrics.png
%doc grub-%{tarversion}/themes/starfield/COPYING.CC-BY-SA-3.0

%files starfield-theme
%{_datarootdir}/grub/themes/starfield

%changelog
* Mon Jun 10 2013 Arkady L. Shane <ashejn@russianfedora.ru> 2.00-18.R
- read OS from rfremix-release first

* Fri May 10 2013 Matthias Clasen <mclasen@redhat.com> - 2.00-18
- Move the starfield theme to a subpackage (#962004)
- Don't allow SSE or MMX on UEFI builds (#949761)

* Wed Apr 24 2013 Peter Jones <pjones@redhat.com> - 2.00-17.pj0
- Rebase to upstream snapshot.

* Thu Apr 04 2013 Peter Jones <pjones@redhat.com> - 2.00-17
- Fix booting from drives with 4k sectors on UEFI.
- Move bash completion to new location (#922997)
- Include lvm support for /boot (#906203)

* Thu Feb 14 2013 Peter Jones <pjones@redhat.com> - 2.00-16
- Allow the user to disable submenu generation
- (partially) support BLS-style configuration stanzas.

* Tue Feb 12 2013 Peter Jones <pjones@redhat.com> - 2.00-15.pj0
- Add various config file related changes.

* Thu Dec 20 2012 Dennis Gilmore <dennis@ausil.us> - 2.00-15
- bump nvr

* Mon Dec 17 2012 Karsten Hopp <karsten@redhat.com> 2.00-14
- add bootpath device to the device list (pfsmorigo, #886685)

* Tue Nov 27 2012 Peter Jones <pjones@redhat.com> - 2.00-13
- Add vlan tag support (pfsmorigo, #871563)
- Follow symlinks during PReP installation in grub2-install (pfsmorigo, #874234)
- Improve search paths for config files on network boot (pfsmorigo, #873406)

* Tue Oct 23 2012 Peter Jones <pjones@redhat.com> - 2.00-12
- Don't load modules when grub transitions to "normal" mode on UEFI.

* Mon Oct 22 2012 Peter Jones <pjones@redhat.com> - 2.00-11
- Rebuild with newer pesign so we'll get signed with the final signing keys.

* Thu Oct 18 2012 Peter Jones <pjones@redhat.com> - 2.00-10
- Various PPC fixes.
- Fix crash fetching from http (gustavold, #860834)
- Issue separate dns queries for ipv4 and ipv6 (gustavold, #860829)
- Support IBM CAS reboot (pfsmorigo, #859223)
- Include all modules in the core image on ppc (pfsmorigo, #866559)

* Mon Oct 01 2012 Peter Jones <pjones@redhat.com> - 1:2.00-9
- Work around bug with using "\x20" in linux command line.
  Related: rhbz#855849

* Thu Sep 20 2012 Peter Jones <pjones@redhat.com> - 2.00-8
- Don't error on insmod on UEFI/SB, but also don't do any insmodding.
- Increase device path size for ieee1275
  Resolves: rhbz#857936
- Make network booting work on ieee1275 machines.
  Resolves: rhbz#857936

* Wed Sep 05 2012 Matthew Garrett <mjg@redhat.com> - 2.00-7
- Add Apple partition map support for EFI

* Thu Aug 23 2012 David Cantrell <dcantrell@redhat.com> - 2.00-6
- Only require pesign on EFI architectures (#851215)

* Tue Aug 14 2012 Peter Jones <pjones@redhat.com> - 2.00-5
- Work around AHCI firmware bug in efidisk driver.
- Move to newer pesign macros
- Don't allow insmod if we're in secure-boot mode.

* Wed Aug 08 2012 Peter Jones <pjones@redhat.com>
- Split module lists for UEFI boot vs UEFI cd images.
- Add raid modules for UEFI image (related: #750794)
- Include a prelink whitelist for binaries that need execstack (#839813)
- Include fix efi memory map fix from upstream (#839363)

* Wed Aug 08 2012 Peter Jones <pjones@redhat.com> - 2.00-4
- Correct grub-mkimage invocation to use efidir RPM macro (jwb)
- Sign with test keys on UEFI systems.
- PPC - Handle device paths with commas correctly.
  Related: rhbz#828740

* Wed Jul 25 2012 Peter Jones <pjones@redhat.com> - 2.00-3
- Add some more code to support Secure Boot, and temporarily disable
  some other bits that don't work well enough yet.
  Resolves: rhbz#836695

* Wed Jul 11 2012 Matthew Garrett <mjg@redhat.com> - 2.00-2
- Set a prefix for the image - needed for installer work
- Provide the font in the EFI directory for the same reason

* Thu Jun 28 2012 Peter Jones <pjones@redhat.com> - 2.00-1
- Rebase to grub-2.00 release.

* Mon Jun 18 2012 Peter Jones <pjones@redhat.com> - 2.0-0.37.beta6
- Fix double-free in grub-probe.

* Wed Jun 06 2012 Peter Jones <pjones@redhat.com> - 2.0-0.36.beta6
- Build with patch19 applied.

* Wed Jun 06 2012 Peter Jones <pjones@redhat.com> - 2.0-0.35.beta6
- More ppc fixes.

* Wed Jun 06 2012 Peter Jones <pjones@redhat.com> - 2.0-0.34.beta6
- Add IBM PPC fixes.

* Mon Jun 04 2012 Peter Jones <pjones@redhat.com> - 2.0-0.33.beta6
- Update to beta6.
- Various fixes from mads.

* Fri May 25 2012 Peter Jones <pjones@redhat.com> - 2.0-0.32.beta5
- Revert builddep change for crt1.o; it breaks ppc build.

* Fri May 25 2012 Peter Jones <pjones@redhat.com> - 2.0-0.31.beta5
- Add fwsetup command (pjones)
- More ppc fixes (IBM)

* Tue May 22 2012 Peter Jones <pjones@redhat.com> - 2.0-0.30.beta5
- Fix the /other/ grub2-tools require to include epoch.

* Mon May 21 2012 Peter Jones <pjones@redhat.com> - 2.0-0.29.beta5
- Get rid of efi_uga and efi_gop, favoring all_video instead.

* Mon May 21 2012 Peter Jones <pjones@redhat.com> - 2.0-0.28.beta5
- Name grub.efi something that's arch-appropriate (kiilerix, pjones)
- use EFI/$SOMETHING_DISTRO_BASED/ not always EFI/redhat/grub2-efi/ .
- move common stuff to -tools (kiilerix)
- spec file cleanups (kiilerix)

* Mon May 14 2012 Peter Jones <pjones@redhat.com> - 2.0-0.27.beta5
- Fix module trampolining on ppc (benh)

* Thu May 10 2012 Peter Jones <pjones@redhat.com> - 2.0-0.27.beta5
- Fix license of theme (mizmo)
  Resolves: rhbz#820713
- Fix some PPC bootloader detection IBM problem
  Resolves: rhbz#820722

* Thu May 10 2012 Peter Jones <pjones@redhat.com> - 2.0-0.26.beta5
- Update to beta5.
- Update how efi building works (kiilerix)
- Fix theme support to bring in fonts correctly (kiilerix, pjones)

* Wed May 09 2012 Peter Jones <pjones@redhat.com> - 2.0-0.25.beta4
- Include theme support (mizmo)
- Include locale support (kiilerix)
- Include html docs (kiilerix)

* Thu Apr 26 2012 Peter Jones <pjones@redhat.com> - 2.0-0.24
- Various fixes from Mads Kiilerich

* Thu Apr 19 2012 Peter Jones <pjones@redhat.com> - 2.0-0.23
- Update to 2.00~beta4
- Make fonts work so we can do graphics reasonably

* Thu Mar 29 2012 David Aquilina <dwa@redhat.com> - 2.0-0.22
- Fix ieee1275 platform define for ppc

* Thu Mar 29 2012 Peter Jones <pjones@redhat.com> - 2.0-0.21
- Remove ppc excludearch lines (dwa)
- Update ppc terminfo patch (hamzy)

* Wed Mar 28 2012 Peter Jones <pjones@redhat.com> - 2.0-0.20
- Fix ppc64 vs ppc exclude according to what dwa tells me they need
- Fix version number to better match policy.

* Tue Mar 27 2012 Dan Horák <dan[at]danny.cz> - 1.99-19.2
- Add support for serial terminal consoles on PPC by Mark Hamzy

* Sun Mar 25 2012 Dan Horák <dan[at]danny.cz> - 1.99-19.1
- Use Fix-tests-of-zeroed-partition patch by Mark Hamzy

* Thu Mar 15 2012 Peter Jones <pjones@redhat.com> - 1.99-19
- Use --with-grubdir= on configure to make it behave like -17 did.

* Wed Mar 14 2012 Peter Jones <pjones@redhat.com> - 1.99-18
- Rebase from 1.99 to 2.00~beta2

* Wed Mar 07 2012 Peter Jones <pjones@redhat.com> - 1.99-17
- Update for newer autotools and gcc 4.7.0
  Related: rhbz#782144
- Add /etc/sysconfig/grub link to /etc/default/grub
  Resolves: rhbz#800152
- ExcludeArch s390*, which is not supported by this package.
  Resolves: rhbz#758333

* Fri Feb 17 2012 Orion Poplawski <orion@cora.nwra.com> - 1:1.99-16
- Build with -Os (bug 782144)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.99-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Matthew Garrett <mjg@redhat.com> - 1.99-14
- fix up various grub2-efi issues

* Thu Dec 08 2011 Adam Williamson <awilliam@redhat.com> - 1.99-13
- fix hardwired call to grub-probe in 30_os-prober (rhbz#737203)

* Mon Nov 07 2011 Peter Jones <pjones@redhat.com> - 1.99-12
- Lots of .spec fixes from Mads Kiilerich:
  Remove comment about update-grub - it isn't run in any scriptlets
  patch info pages so they can be installed and removed correctly when renamed
  fix references to grub/grub2 renames in info pages (#743964)
  update README.Fedora (#734090)
  fix comments for the hack for upgrading from grub2 < 1.99-4
  fix sed syntax error preventing use of $RPM_OPT_FLAGS (#704820)
  make /etc/grub2*.cfg %config(noreplace)
  make grub.cfg %ghost - an empty file is of no use anyway
  create /etc/default/grub more like anaconda would create it (#678453)
  don't create rescue entries by default - grubby will not maintain them anyway
  set GRUB_SAVEDEFAULT=true so saved defaults works (rbhz#732058)
  grub2-efi should have its own bash completion
  don't set gfxpayload in efi mode - backport upstream r3402
- Handle dmraid better. Resolves: rhbz#742226

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.99-11
- Rebuilt for glibc bug#747377

* Wed Oct 19 2011 Adam Williamson <awilliam@redhat.com> - 1.99-10
- /etc/default/grub is explicitly intended for user customization, so
  mark it as config(noreplace)

* Tue Oct 11 2011 Peter Jones <pjones@redhat.com> - 1.99-9
- grub has an epoch, so we need that expressed in the obsolete as well.
  Today isn't my day.

* Tue Oct 11 2011 Peter Jones <pjones@redhat.com> - 1.99-8
- Fix my bad obsoletes syntax.

* Thu Oct 06 2011 Peter Jones <pjones@redhat.com> - 1.99-7
- Obsolete grub
  Resolves: rhbz#743381

* Wed Sep 14 2011 Peter Jones <pjones@redhat.com> - 1.99-6
- Use mv not cp to try to avoid moving disk blocks around for -5 fix
  Related: rhbz#735259
- handle initramfs on xen better (patch from Marko Ristola)
  Resolves: rhbz#728775

* Sat Sep 03 2011 Kalev Lember <kalevlember@gmail.com> - 1.99-5
- Fix upgrades from grub2 < 1.99-4 (#735259)

* Fri Sep 02 2011 Peter Jones <pjones@redhat.com> - 1.99-4
- Don't do sysadminny things in %preun or %post ever. (#735259)
- Actually include the changelog in this build (sorry about -3)

* Thu Sep 01 2011 Peter Jones <pjones@redhat.com> - 1.99-2
- Require os-prober (#678456) (patch from Elad Alfassa)
- Require which (#734959) (patch from Elad Alfassa)

* Thu Sep 01 2011 Peter Jones <pjones@redhat.com> - 1.99-1
- Update to grub-1.99 final.
- Fix crt1.o require on x86-64 (fix from Mads Kiilerich)
- Various CFLAGS fixes (from Mads Kiilerich)
  - -fexceptions and -m64
- Temporarily ignore translations (from Mads Kiilerich)

* Thu Jul 21 2011 Peter Jones <pjones@redhat.com> - 1.99-0.3
- Use /sbin not /usr/sbin .

* Thu Jun 23 2011 Peter Lemenkov <lemenkov@gmail.com> - 1:1.99-0.2
- Fixes for ppc and ppc64

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.98-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
